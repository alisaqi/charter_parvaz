# coding=utf8

import pyromod.listen
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import FloodWait
from charterTicket import flights_handler
from persiantools.jdatetime import JalaliDate, JalaliDateTime
from pykeyboard import InlineKeyboard, InlineButton
import logging
import asyncio
import datetime
import pytz
import config


# Initialize the bot client with credentials from config
app = Client(
    "Charter_ticketbot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# Global state - consider using a database for production
users_database = {}
flights_result = {}
flight_date = None
destination_city = None
departure_city = None
next_flight_result_iter = 0


def jalali_dates(today, days=30):
    """
    Generate a dictionary of Jalali dates starting from today.
    
    Args:
        today: The starting JalaliDate
        days: Number of days to generate (default: 30)
    
    Returns:
        dict: Dictionary with index as key and ISO formatted date as value
    """
    dates = {}
    for i in range(days):
        dates[i] = (JalaliDate(today) + datetime.timedelta(days=i)).isoformat()
    return dates


@app.on_message(filters.command('start') & filters.private)
async def check_user(client, message):
    """Handle /start command and verify channel membership."""
    global users_database
    try:
        if message.from_user.id not in users_database.keys():
            await app.send_message(
                chat_id=message.chat.id,
                text='سلام به ربات Charter Parvaz خوش آمدید\n\n⚠️ شما هنوز عضو کانال ما نشدین، لطفا جهت ادامه فعالیت روی دکمه زیر کلیک کنید.',
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "عضویت در کانال",
                                url="https://t.me/parvaz_charters"
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                "عضو کانال شدم",
                                callback_data="membershipApproval",
                            )
                        ],
                    ]
                )
            )
        elif message.from_user.id in users_database.keys():
            await start_menu(client, message)

    except Exception as ex:
        logging.error(f"Error in check_user: {ex}", exc_info=True)
        await app.send_message(
            chat_id=message.chat.id,
            text='خطایی رخ داده است. لطفا دوباره تلاش کنید.'
        )


@app.on_message(filters.private)
async def user_manager(client, message):
    """Handle user profile management."""
    try:
        await app.send_message(
            chat_id=message.chat.id,
            text='شما در این بخش می توانید پروفایل کاربری خود را مدیریت کنید.\nلطفا یکی از گزینه های زیر را انتخاب کنید',
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("ویرایش اطلاعات", callback_data="create_user_account")],
                    [InlineKeyboardButton("بازگشت به منوی اصلی 🏠", callback_data="backToMain")]
                ]
            )
        )
    except Exception as ex:
        logging.error(f"Error in user_manager: {ex}", exc_info=True)

@app.on_message(filters.private)
async def start_menu(client, message):
    """Display main menu to the user."""
    try:
        answer = await app.ask(
            chat_id=message.chat.id,
            text='لطفا یکی از خدمات زیر را انتخاب کنید',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ["بلیط هواپیما ✈️"],
                    ["بلیط اتوبوس 🚌"],
                    ["بلیط قطار 🚆"],
                    ["پروفایل کاربری 📝"],
                    ["ارتباط با ما 📩"],
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            ))

        if answer.text == "بلیط هواپیما ✈️":
            await flight_order(client, message)
        elif answer.text == "بلیط اتوبوس 🚌":
            await app.send_message(chat_id=message.chat.id, text='این بخش فعلا فعال نیست ⚠️')
            await start_menu(client, message)
        elif answer.text == "بلیط قطار 🚆":
            await app.send_message(chat_id=message.chat.id, text='این بخش فعلا فعال نیست ⚠️')
            await start_menu(client, message)
        elif answer.text == "پروفایل کاربری 📝":
            await user_manager(client, message)
        elif answer.text == "ارتباط با ما 📩":
            await app.send_message(
                chat_id=message.chat.id,
                text='شما می توانید از طریق یکی از روش های زیر با ما در ارتباط باشید',
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("تلگرام", url=config.CONTACT_URL)],
                        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠", callback_data="backToMain")]
                    ]
                )
            )
    except Exception as ex:
        logging.error(f"Error in start_menu: {ex}", exc_info=True)

@app.on_message(filters.private)
async def flight_order(client, message):
    """Handle flight order selection."""
    try:
        answer = await app.ask(
            chat_id=message.chat.id,
            text='لطفا نوع پرواز خود را انتخاب کنید',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ["پرواز داخلی 🇮🇷"],
                    ["پرواز خارجی 🌍"],
                    ["بازگشت به منوی اصلی 🏠"],
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            ))

        if answer.text == "پرواز داخلی 🇮🇷":
            await domestic_flight_order(client, message)
        elif answer.text == "پرواز خارجی 🌍":
            await international_flight_order(client, message)
        elif answer.text == "بازگشت به منوی اصلی 🏠":
            await start_menu(client, message)
    except Exception as ex:
        logging.error(f"Error in flight_order: {ex}", exc_info=True)

@app.on_message(filters.private)
async def domestic_flight_order(client, message):
    """Handle domestic flight order."""
    global flights_result, flight_date, departure_city, destination_city

    try:
        # Get sorted domestic cities
        domestic_cities = sorted(
            [city for city in config.cities.keys() if config.cities[city]['type']['domestic']],
            key=lambda city: config.cities[city]['type']['domesticId']
        )
        
        departure_city = await app.ask(
            chat_id=message.chat.id,
            text='لطفا مبدا خود را انتخاب کنید',
            reply_markup=ReplyKeyboardMarkup(
                [[city] for city in domestic_cities],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        # Filter out selected departure city from destinations
        destination_cities = [
            city for city in domestic_cities 
            if config.cities[city]['name'] != departure_city.text
        ]
        
        destination_city = await app.ask(
            chat_id=message.chat.id,
            text='لطفا مقصد خود را انتخاب کنید',
            reply_markup=ReplyKeyboardMarkup(
                [[city] for city in destination_cities],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        flight_date = await app.ask(
            chat_id=message.chat.id,
            text='لطفا تاریخ سفر خود را انتخاب کنید',
            reply_markup=ReplyKeyboardMarkup(
                [[dates] for dates in jalali_dates(JalaliDate.today()).values()],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        previous_message = await app.send_message(
            chat_id=message.chat.id,
            text="ربات در حال گرفتن اطلاعات پرواز ها می باشد 🚀"
        )

        flights_result = flights_handler(
            departureCity=config.cities[departure_city.text]['title'],
            destinationCity=config.cities[destination_city.text]['title'],
            dateOrder=flight_date.text
        )

        await flights_result_show(client, message, previous_message.id, nextMessage=True, previousMessage=False)

    except Exception as ex:
        logging.error(f"Error in domestic_flight_order: {ex}", exc_info=True)

@app.on_message(filters.private)
async def international_flight_order(client, message):
    """Handle international flight order."""
    global flights_result, flight_date, departure_city, destination_city

    try:
        # Get sorted international cities
        international_cities = sorted(
            [city for city in config.cities.keys() if config.cities[city]['type']['international']],
            key=lambda city: config.cities[city]['type']['internationalId']
        )
        
        departure_city = await app.ask(
            chat_id=message.chat.id,
            text='لطفا مبدا خود را انتخاب کنید',
            reply_markup=ReplyKeyboardMarkup(
                [[city] for city in international_cities],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        # Filter destinations based on departure city type
        if config.cities[departure_city.text]['type']['domestic']:
            destination_cities = [
                city for city in international_cities
                if config.cities[city]['name'] != departure_city.text 
                and not config.cities[city]['type']['domestic']
            ]
        else:
            destination_cities = [
                city for city in international_cities
                if config.cities[city]['name'] != departure_city.text 
                and config.cities[city]['type']['domestic']
            ]

        destination_city = await app.ask(
            chat_id=message.chat.id,
            text='لطفا مقصد خود را انتخاب کنید:',
            reply_markup=ReplyKeyboardMarkup(
                [[city] for city in destination_cities],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        flight_date = await app.ask(
            chat_id=message.chat.id,
            text='لطفا تاریخ سفر خود را انتخاب کنید',
            reply_markup=ReplyKeyboardMarkup(
                [[dates] for dates in jalali_dates(JalaliDate.today()).values()],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        previous_message = await app.send_message(
            chat_id=message.chat.id,
            text="ربات در حال گرفتن اطلاعات پرواز ها می باشد 🚀"
        )

        flights_result = flights_handler(
            departureCity=config.cities[departure_city.text]['title'],
            destinationCity=config.cities[destination_city.text]['title'],
            dateOrder=flight_date.text
        )

        await flights_result_show(client, message, previous_message.id, nextMessage=True, previousMessage=False)

    except Exception as ex:
        logging.error(f"Error in international_flight_order: {ex}", exc_info=True)


def create_navigation_buttons(is_first, is_last, has_multiple):
    """
    Create navigation buttons for flight results pagination.
    
    Args:
        is_first: Whether this is the first result
        is_last: Whether this is the last result
        has_multiple: Whether there are multiple results
    
    Returns:
        list: List of button rows for InlineKeyboardMarkup
    """
    buttons = []
    
    # Purchase button (always present)
    buttons.append([InlineKeyboardButton("خرید این بلیط 🛒", url=config.CONTACT_URL)])
    
    # Navigation buttons
    nav_buttons = []
    if not is_first and has_multiple:
        nav_buttons.append(InlineKeyboardButton("⬅️ بلیط قبلی", callback_data="previousFlightResult"))
    if not is_last and has_multiple:
        nav_buttons.append(InlineKeyboardButton("➡️ بلیط بعدی", callback_data="nextFlightResult"))
    
    if nav_buttons:
        buttons.append(nav_buttons)
    
    # Common buttons
    buttons.append([InlineKeyboardButton("جستجو جدید 🔍", callback_data="newFlightSearch")])
    buttons.append([InlineKeyboardButton("بازگشت به منوی اصلی 🏠", callback_data="backToMain")])
    
    return buttons


@app.on_message(filters.private)
async def flights_result_show(client, message, previousMessageID, nextMessage, previousMessage):
    """Display flight results with pagination."""
    global next_flight_result_iter, flights_result, flight_date, destination_city, departure_city

    try:
        if flights_result and flights_result is not False:
            current_flight = flights_result[next_flight_result_iter]
            commission = config.flights_commission.get(current_flight['ticketType'], 0.05) + 1
            
            # Calculate final price with commission
            final_price = int(float(current_flight['priceDigit'] * commission))
            
            # Build flight info text
            flight_text = (
                f"پرواز {departure_city.text} 🛫 به {destination_city.text} 🛬\n\n"
                f"✈️ شماره پرواز : {current_flight['flightNumber']}\n\n"
                f"🎫 نوع بلیط : {current_flight['ticketType']}\n\n"
                f"💵 قیمت : {final_price:,} تومان\n\n"
                f"📅 تاریخ و ساعت پرواز: \n{flight_date.text}\n{current_flight['departure']}\n"
                f"💺 تعداد صندلی خالی: {current_flight['freeSeats']}\n\n"
                f"🌐 هواپیمایی: {current_flight['company']}"
            )
            
            # Determine pagination state
            result_keys = list(flights_result.keys())
            is_first = next_flight_result_iter == result_keys[0]
            is_last = next_flight_result_iter == result_keys[-1]
            has_multiple = len(result_keys) > 1
            
            # Create navigation buttons
            reply_markup = InlineKeyboardMarkup(
                create_navigation_buttons(is_first, is_last, has_multiple)
            )
            
            await app.edit_message_text(
                chat_id=message.chat.id,
                message_id=previousMessageID,
                text=flight_text,
                reply_markup=reply_markup
            )
        else:
            # No flights found
            await app.edit_message_text(
                chat_id=message.chat.id,
                message_id=previousMessageID,
                text="⚠️ متاسفانه هیچ بلیطی یافت نشد",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("جستجو جدید 🔍", callback_data="newFlightSearch")],
                        [InlineKeyboardButton("بازگشت به منوی اصلی 🏠", callback_data="backToMain")],
                    ]
                )
            )
    except Exception as ex:
        logging.error(f"Error in flights_result_show: {ex}", exc_info=True)


@app.on_callback_query()
async def callback_query_handler(client, callback_query):
    """Handle callback queries from inline buttons."""
    global next_flight_result_iter, users_database

    try:
        if callback_query.data == "membershipApproval":
            list_members = []
            async for members in app.get_chat_members(chat_id=config.channels_ids["Parvaz_charters"]):
                list_members.append(members.user.id)

            if callback_query.from_user.id in list_members:
                if callback_query.from_user.id not in users_database:
                    users_database[callback_query.from_user.id] = {
                        "username": callback_query.from_user.username,
                        "firstName": callback_query.from_user.first_name,
                        "id": callback_query.from_user.id,
                        "membership": True,
                        "membershipDate": datetime.datetime.now(pytz.timezone('Asia/Tehran')).strftime(
                            "%Y-%m-%d %H:%M:%S"),
                    }
                await app.edit_message_text(
                    chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.id,
                    text='عضویت شما تایید شد ✅',
                )
                await start_menu(client, callback_query.message)
            else:
                await app.edit_message_text(
                    chat_id=callback_query.message.chat.id,
                    message_id=callback_query.message.id,
                    text='⚠️ عضویت شما در کانال تایید نشد. لطفا ابتدا در کانال عضو شوید و سپس دوباره روی /start کلیک کنید.',
                )

        elif callback_query.data == "create_user_account":
            await app.delete_messages(chat_id=callback_query.message.chat.id, message_ids=callback_query.message.id)

            # Get and validate farsi name
            while True:
                farsi_name = await app.ask(
                    chat_id=callback_query.from_user.id,
                    text="لطفا نام و نام خانوادگی خود را به فارسی ارسال کنید:",
                )
                if config.validate_persian_name(farsi_name.text):
                    break
                await app.send_message(
                    chat_id=callback_query.from_user.id,
                    text="⚠️ نام فارسی نامعتبر است. لطفا فقط از حروف فارسی استفاده کنید."
                )
            
            # Get and validate english name
            while True:
                english_name = await app.ask(
                    chat_id=callback_query.from_user.id,
                    text="لطفا نام و نام خانوادگی خود را به انگلیسی ارسال کنید (دقت کنید که اسم شما باید منطبق با اطلاعات درج شده در پاسپورت شما باشد) :",
                )
                if config.validate_english_name(english_name.text):
                    break
                await app.send_message(
                    chat_id=callback_query.from_user.id,
                    text="⚠️ نام انگلیسی نامعتبر است. لطفا فقط از حروف انگلیسی استفاده کنید."
                )
            
            # Get and validate phone number
            while True:
                phone_number = await app.ask(
                    chat_id=callback_query.from_user.id,
                    text="لطفا شماره تلفن همراه خود را ارسال کنید (مثال: 09123456789):",
                )
                if config.validate_phone_number(phone_number.text):
                    break
                await app.send_message(
                    chat_id=callback_query.from_user.id,
                    text="⚠️ شماره تلفن نامعتبر است. لطفا شماره موبایل 11 رقمی خود را وارد کنید."
                )
            
            # Get and validate national ID
            while True:
                national_id = await app.ask(
                    chat_id=callback_query.from_user.id,
                    text="لطفا کد ملی 10 رقمی خود را ارسال کنید:",
                )
                if config.validate_national_id(national_id.text):
                    break
                await app.send_message(
                    chat_id=callback_query.from_user.id,
                    text="⚠️ کد ملی نامعتبر است. لطفا کد ملی 10 رقمی خود را وارد کنید."
                )
            
            # Get and validate passport number
            while True:
                passport_number = await app.ask(
                    chat_id=callback_query.from_user.id,
                    text="لطفا شماره پاسپورت خود را ارسال کنید (درصورتی که پاسپورت ندارید، عدد صفر را وارد کنید) :",
                )
                if config.validate_passport(passport_number.text):
                    break
                await app.send_message(
                    chat_id=callback_query.from_user.id,
                    text="⚠️ شماره پاسپورت نامعتبر است. لطفا شماره پاسپورت معتبر یا عدد 0 را وارد کنید."
                )
            
            # Store user data with consistent formatting
            users_database[callback_query.from_user.id] = {
                "username": callback_query.from_user.username,
                "farsi_name": farsi_name.text.strip(),
                "english_name": english_name.text.strip().title(),  # Capitalize names
                "phone_number": phone_number.text.strip().replace(' ', ''),  # Remove spaces
                "national_id": national_id.text.strip(),
                "passport_number": passport_number.text.strip().upper(),  # Uppercase for passport
            }

            await app.send_message(chat_id=callback_query.from_user.id, text="اطلاعات شما با موفقیت ثبت شد ✅")
            await start_menu(client, callback_query.message)

        elif callback_query.data == "nextFlightResult":
            next_flight_result_iter += 1
            await flights_result_show(client, callback_query.message, callback_query.message.id, nextMessage=True, previousMessage=False)

        elif callback_query.data == "previousFlightResult":
            next_flight_result_iter -= 1
            await flights_result_show(client, callback_query.message, callback_query.message.id, nextMessage=False, previousMessage=True)

        elif callback_query.data == "lastFlightResult":
            next_flight_result_iter -= 1
            await flights_result_show(client, callback_query.message, callback_query.message.id, nextMessage=False, previousMessage=True)

        elif callback_query.data == "firstFlightResult":
            next_flight_result_iter += 1
            await flights_result_show(client, callback_query.message, callback_query.message.id, nextMessage=True, previousMessage=False)

        elif callback_query.data == "newFlightSearch":
            next_flight_result_iter = 0
            await flight_order(client, callback_query.message)

        elif callback_query.data == "backToMain":
            next_flight_result_iter = 0
            await start_menu(client, callback_query.message)

    except Exception as ex:
        logging.error(f"Error in callback_query_handler: {ex}", exc_info=True)


# Configure logging
logging.basicConfig(
    format=config.LOGGING_FORMAT,
    filename=config.LOG_FILE,
    level=logging.INFO
)

# Main execution
if __name__ == "__main__":
    try:
        print("Bot is starting...")
        app.run()
    except Exception as ex:
        logging.error(f"Fatal error: {ex}", exc_info=True)
        try:
            app.send_document(
                chat_id="ASoDme",
                document=config.LOG_FILE,
                caption="Log file for charter ticket Bot",
            )
        except Exception as send_ex:
            logging.error(f"Failed to send log file: {send_ex}", exc_info=True)
