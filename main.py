# coding=utf8

import pyromod.listen
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import FloodWait
from charterTicket import flights_handler
from persiantools.jdatetime import JalaliDate, JalaliDateTime
from pyrogram import Client, filters
from pykeyboard import InlineKeyboard, InlineButton
import logging
import asyncio
import datetime
import pytz
import config


app = Client("Charter_ticketbot",
             api_id=14244400,
             api_hash="118639cb7a29cf67eb5e45a4251a8aa4",
             bot_token= "5633146247:AAGppS_-l-pKkxiq_goCs9-Wme7WaZWF6ik"
             )


usersDatabase = {}
flights_result = {}
flight_date = 0
destination_city = None
departure_city = None
next_flight_result_Iter = 0

def jalali_dates(today):
    dates = {}
    i = 0
    while i < 30:
        dates[i] = (JalaliDate(today) + datetime.timedelta(days=i)).isoformat()
        i += 1
    return dates


@app.on_message(filters.command('start') & filters.private)
async def check_user(client, message):
    global usersDatabase
    try:
        if message.from_user.id not in usersDatabase.keys():
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

            # await app.send_message(
            #     chat_id=message.chat.id,
            #     text= 'سلام به ربات Charter Parvaz خوش آمدید\n\n⚠️ پیش از شروع به کار نیاز هست تا پروفایل کاربری خود را در ربات ایجاد کنید\n\n⚠️ در نظر داشته باشید که اطلاعات شما صرفا جهت رزرو بلیط مورد استفاده قرار می گیرد، پس لطفا در ورود اطلاعات دقت کنید.',
            #     reply_markup=InlineKeyboardMarkup(
            #         [
            #             [
            #                 InlineKeyboardButton(
            #                     "ساخت حساب کاربری",
            #                     callback_data="create_user_account",
            #                 )
            #             ]
            #         ]
            #     )
            # )

        elif message.from_user.id in usersDatabase.keys():
            await start_menu(client, message)

    except Exception as ex:
        print(logging.ERROR, ex)
        pass


@app.on_message(filters.private)
async def user_manager(client, message):
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
        print(logging.ERROR, ex)
        pass

@app.on_message(filters.private)
async def start_menu(client, message):
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
            await app.send_message(chat_id=message.chat.id,
                                   text='شما می توانید از طریق یکی از روش های زیر با ما در ارتباط باشید',
                                   reply_markup=InlineKeyboardMarkup(
                                       [
                                                # [InlineKeyboardButton("اینستاگرام", url="https://instagram.com/parvaz_charters")],
                                                [InlineKeyboardButton("تلگرام", url="https://t.me/ASoDme")],
                                                # [InlineKeyboardButton("وبسایت", url="https://parvazcharters.com")],
                                                [InlineKeyboardButton("بازگشت به منوی اصلی 🏠", callback_data="backToMain")]
                                       ]
                                   )
                                   )

    except Exception as ex:
        print(logging.ERROR, ex)
        pass

@app.on_message(filters.private)
async def flight_order (client, message):
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
        print(logging.ERROR, ex)
        pass

@app.on_message(filters.private)
async def domestic_flight_order (client, message):
    global flights_result
    global flight_date
    global departure_city
    global destination_city

    try:
        departure_city = await app.ask (
            chat_id=message.chat.id,
            text='لطفا مبدا خود را انتخاب کنید',
            reply_markup=ReplyKeyboardMarkup(
                [
                    [city] for city in sorted(config.cities.keys(), key=lambda city: config.cities[city]['type']['domesticId']) if config.cities[city]['type']['domestic'] == True
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        destination_city = await app.ask(
            chat_id=message.chat.id,
            text='لطفا مقصد خود را انتخاب کنید',
            reply_markup=ReplyKeyboardMarkup(
                [
                    [city] for city in sorted(config.cities.keys(), key=lambda city: config.cities[city]['type']['domesticId']) if config.cities[city]['name'] != departure_city.text and config.cities[city]['type']['domestic'] == True
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        flight_date = await app.ask (
            chat_id=message.chat.id,
            text='لطفا تاریخ سفر خود را انتخاب کنید',
            reply_markup=ReplyKeyboardMarkup(
                [
                    [dates] for dates in jalali_dates(JalaliDate.today()).values()
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        previousMessage = await app.send_message(
            chat_id=message.chat.id,
            text="ربات در حال گرفتن اطلاعات پرواز ها می باشد 🚀"
        )

        flights_result = flights_handler(departureCity= config.cities[departure_city.text]['title'],
                                         destinationCity= config.cities[destination_city.text]['title'],
                                         dateOrder= flight_date.text)

        # print(flightsResult)
        await flights_result_show(client, message, previousMessage.id, nextMessage= True, previousMessage= False)


    except Exception as ex:
        print(logging.ERROR, ex)
        pass

@app.on_message(filters.private)
async def international_flight_order (client, message):
    global flights_result
    global flight_date
    global departure_city
    global destination_city

    try:
        departure_city = await app.ask (
            chat_id=message.chat.id,
            text='لطفا مبدا خود را انتخاب کنید',
            reply_markup=ReplyKeyboardMarkup(
                [
                    [city] for city in sorted(config.cities.keys(), key=lambda city: config.cities[city]['type']['internationalId']) if config.cities[city]['type']['international'] == True
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        if config.cities[departure_city.text]['type']['domestic'] == True:
            destination_city = await app.ask(
                chat_id=message.chat.id,
                text='لطفا مقصد خود را انتخاب کنید:',
                reply_markup=ReplyKeyboardMarkup(
                    [
                        [city] for city in sorted(config.cities.keys(), key=lambda city: config.cities[city]['type']['internationalId']) if config.cities[city]['name'] != departure_city.text and config.cities[city]['type']['international'] == True and config.cities[city]['type']['domestic'] == False
                    ],
                    resize_keyboard=True,
                    one_time_keyboard=True
                )
            )
        elif config.cities[departure_city.text]['type']['domestic'] == False:
            destination_city = await app.ask(
                chat_id=message.chat.id,
                text='لطفا مقصد خود را انتخاب کنید:',
                reply_markup=ReplyKeyboardMarkup(
                    [
                        [city] for city in sorted(config.cities.keys(), key=lambda city: config.cities[city]['type']['internationalId']) if config.cities[city]['name'] != departure_city.text and config.cities[city]['type']['international'] == True and config.cities[city]['type']['domestic'] == True
                    ],
                    resize_keyboard=True,
                    one_time_keyboard=True
                )
            )

        flight_date = await app.ask (
            chat_id=message.chat.id,
            text='لطفا تاریخ سفر خود را انتخاب کنید',
            reply_markup=ReplyKeyboardMarkup(
                [
                    [dates] for dates in jalali_dates(JalaliDate.today()).values()
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        previousMessage = await app.send_message(
            chat_id=message.chat.id,
            text="ربات در حال گرفتن اطلاعات پرواز ها می باشد 🚀"
        )

        flights_result = flights_handler(departureCity= config.cities[departure_city.text]['title'],
                                         destinationCity= config.cities[destination_city.text]['title'],
                                         dateOrder= flight_date.text)

        # print(flightsResult)
        await flights_result_show(client, message, previousMessage.id, nextMessage= True, previousMessage= False)


    except Exception as ex:
        print(logging.ERROR, ex)
        pass

@app.on_message(filters.private)
async def flights_result_show (client, message, previousMessageID, nextMessage, previousMessage):
    global next_flight_result_Iter
    global flights_result
    global flight_date
    global destination_city
    global departure_city


    # try:
    #     while nextFlightResultIter < len(flightsResult.keys()):
    #         result = await app.edit_message_text(
    #             chat_id=message.chat.id,
    #             message_id=editMessage.id,
    #             text=f"شماره پرواز: {flightsResult[nextFlightResultIter]['flightNumber']}\n\nقیمت : {flightsResult[nextFlightResultIter]['price']}\nتاریخ پرواز: {flightDate.text}\nساعت پرواز: {flightsResult[nextFlightResultIter]['departure']}\n\nتعداد صندلی خالی: {flightsResult[nextFlightResultIter]['freeSeats']}\n\nهواپیمایی: {flightsResult[nextFlightResultIter]['company']}",
    #             reply_markup=InlineKeyboardMarkup(
    #                 [
    #                     [
    #                         InlineKeyboardButton(
    #                             "خرید این بلیط 🛒",
    #                             callback_data="purchesTicket"
    #                         )
    #                     ],
    #                 ]
    #             )
    #         )
    try:
        if flights_result != False:
            commission = config.flightsCommision[flights_result[next_flight_result_Iter]['ticketType']] + 1
            lastResultId = list(flights_result.keys())[-1]
            firstResultId = list(flights_result.keys())[0]
            purchase_url = 'https://t.me/ASoDme'
            # purchaseUrl = 'http://ticket-charter.com/Ticket' + '-' + config.cities[departureCity.text]['title'] + '-' + config.cities[destinationCity.text]['title'] + '.html' + '?' + 't='  + flightDate.text
            finalText = f"پرواز {departure_city.text} 🛫 به {destination_city.text} 🛬\n\n✈️ شماره پرواز : {flights_result[next_flight_result_Iter]['flightNumber']}\n\n🎫 نوع بلیط : {flights_result[next_flight_result_Iter]['ticketType']}\n\n💵 قیمت : {int(float(flights_result[next_flight_result_Iter]['priceDigit'] * commission)):,} تومان\n\n📅 تاریخ و ساعت پرواز: \n{flight_date.text}\n{flights_result[next_flight_result_Iter]['departure']}\n💺 تعداد صندلی خالی: {flights_result[next_flight_result_Iter]['freeSeats']}\n\n🌐 هواپیمایی: {flights_result[next_flight_result_Iter]['company']}"

            if previousMessage == False and nextMessage == True and list(flights_result.keys())[next_flight_result_Iter] == (firstResultId) and len(flights_result.keys()) > 1:
                await app.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=previousMessageID,
                    text=finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url=purchase_url
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "➡️ بلیط بعدی",
                                    callback_data="firstFlightResult"
                                )

                            ],
                            [
                                InlineKeyboardButton(
                                    "جستجو جدید 🔍",
                                    callback_data="newFlightSearch"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "بازگشت به منوی اصلی 🏠",
                                    callback_data="backToMain"
                                )
                            ],

                        ]

                    )
                )
            elif previousMessage == False and nextMessage == True and list(flights_result.keys())[next_flight_result_Iter] == (firstResultId) and len(flights_result.keys()) == 1:
                await app.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=previousMessageID,
                    text=finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url=purchase_url
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "جستجو جدید 🔍",
                                    callback_data="newFlightSearch"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "بازگشت به منوی اصلی 🏠",
                                    callback_data="backToMain"
                                )
                            ],

                        ]

                    )
                )
            elif previousMessage == True and nextMessage == False and list(flights_result.keys())[next_flight_result_Iter] == (lastResultId):
                await app.edit_message_text(
                    chat_id = message.chat.id,
                    message_id = previousMessageID,
                    text= finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url= purchase_url
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "⬅️ بلیط قبلی",
                                    callback_data="lastFlightResult"
                                ),

                            ],
                            [
                                InlineKeyboardButton(
                                    "جستجو جدید 🔍",
                                    callback_data="newFlightSearch"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "بازگشت به منوی اصلی 🏠",
                                    callback_data="backToMain"
                                )
                            ]
                        ]
                    )
                )
            elif previousMessage == False and nextMessage == True and list(flights_result.keys())[next_flight_result_Iter] != firstResultId and list(flights_result.keys())[next_flight_result_Iter] != lastResultId:
                await app.edit_message_text(
                    chat_id = message.chat.id,
                    message_id = previousMessageID,
                    text=finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url= purchase_url
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "⬅️ بلیط قبلی",
                                    callback_data="previousFlightResult"
                                ),
                                InlineKeyboardButton(
                                    "➡️ بلیط بعدی",
                                    callback_data="nextFlightResult"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "جستجو جدید 🔍",
                                    callback_data="newFlightSearch"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "بازگشت به منوی اصلی 🏠",
                                    callback_data="backToMain"
                                )
                            ]
                        ]
                    )
                )
            elif previousMessage == False and nextMessage == True and list(flights_result.keys())[next_flight_result_Iter] != firstResultId and list(flights_result.keys())[next_flight_result_Iter] == lastResultId:

                await app.edit_message_text(
                    chat_id = message.chat.id,
                    message_id = previousMessageID,
                    text=finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url= purchase_url
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "⬅️ بلیط قبلی",
                                    callback_data="previousFlightResult"
                                ),
                            ],
                            [
                                InlineKeyboardButton(
                                    "جستجو جدید 🔍",
                                    callback_data="newFlightSearch"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "بازگشت به منوی اصلی 🏠",
                                    callback_data="backToMain"
                                )
                            ]
                        ]
                    )
                )
            elif previousMessage == True and nextMessage == False and list(flights_result.keys())[next_flight_result_Iter] != firstResultId and list(flights_result.keys())[next_flight_result_Iter] != lastResultId:
                await app.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=previousMessageID,
                    text=finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url= purchase_url
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "⬅️ بلیط قبلی",
                                    callback_data="previousFlightResult"
                                ),
                                InlineKeyboardButton(
                                    "➡️ بلیط بعدی",
                                    callback_data="nextFlightResult"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "جستجو جدید 🔍",
                                    callback_data="newFlightSearch"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "بازگشت به منوی اصلی 🏠",
                                    callback_data="backToMain"
                                )
                            ]
                        ]
                    )
                )
            elif previousMessage == True and nextMessage == False and list(flights_result.keys())[next_flight_result_Iter] == firstResultId and list(flights_result.keys())[next_flight_result_Iter] != lastResultId:
                await app.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=previousMessageID,
                    text=finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url= purchase_url
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "➡️ بلیط بعدی",
                                    callback_data="nextFlightResult"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "جستجو جدید 🔍",
                                    callback_data="newFlightSearch"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "بازگشت به منوی اصلی 🏠",
                                    callback_data="backToMain"
                                )
                            ]
                        ]
                    )
                )

        elif flights_result == False:
            await app.edit_message_text(
                chat_id=message.chat.id,
                message_id=previousMessageID,
                text="⚠️ متاسفانه هیچ بلیطی یافت نشد",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "جستجو جدید 🔍",
                                callback_data="newFlightSearch"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "بازگشت به منوی اصلی 🏠",
                                callback_data="backToMain"
                            )
                        ],

                    ]
                )
            )
    except Exception as ex:
        print(logging.error(ex))
        pass


@app.on_callback_query()
async def callback_query_handler(client, callback_query):
    global next_flight_result_Iter
    global usersDatabase

    try:
        if callback_query.data == "membershipApproval":
            async for members in app.get_chat_members(chat_id=config.channelsIDs["Parvaz_charters"]):
                if members.user.id == callback_query.from_user.id:
                    foundUser = True
                    if callback_query.from_user.id in usersDatabase:
                        usersDatabase[callback_query.from_user.id] = {
                            "username": callback_query.from_user.username,
                            "firstName": callback_query.from_user.first_name,
                            "id": callback_query.from_user.id,
                            "membership": True,
                            "membershipDate": datetime.datetime.now(pytz.timezone('Asia/Tehran')).strftime("%Y-%m-%d %H:%M:%S"),
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
                            text='⚠️ عضویت شما در کانال تایید نشد. لطفا ابتدا در کانال عضو شوید و سپس دوباره اقدام به تایید عضویت کنید',
                        )
                        await callback_query_handler(client, callback_query)

        elif callback_query.data == "create_user_account":
            try:
                await app.delete_messages(chat_id=callback_query.message.chat.id, message_ids=callback_query.message.id)

                farsi_name = await app.ask(
                    chat_id=callback_query.from_user.id,
                    text="لطفا نام و نام خانوادگی خود را به فارسی ارسال کنید:",
                )
                english_name = await app.ask(
                    chat_id=callback_query.from_user.id,
                    text="لطفا نام و نام خانوادگی خود را به انگلیسی ارسال کنید (دقت کنید که اسم شما باید منطبق با اطلاعات درج شده در پاسپورت شما باشد) :",
                )
                phone_number = await app.ask(
                    chat_id=callback_query.from_user.id,
                    text="لطفا شماره تلفن همراه خود را ارسال کنید :",
                )
                national_id = await app.ask(
                    chat_id=callback_query.from_user.id,
                    text="لطفا کد ملی خود را ارسال کنید :",
                )
                passport_number = await app.ask(
                    chat_id=callback_query.from_user.id,
                    text="لطفا شماره پاسپورت خود را ارسال کنید (درصورتی که پاسپورت ندارید، عدد صفر را وارد کنید) :",
                )
                usersDatabase[callback_query.from_user.id] = {
                    "username": callback_query.from_user.username,
                    "farsi_name": farsi_name.text,
                    "english_name": english_name.text,
                    "phone_number": phone_number.text,
                    "national_id": national_id.text,
                    "passport_number": passport_number.text,
                }

                # if user's data is stored in userDatabase successfully, return to start menu
                if callback_query.from_user.id in usersDatabase.keys():
                    await app.send_message(chat_id=callback_query.from_user.id, text="اطلاعات شما با موفقیت ثبت شد ✅")
                    # print(usersDatabase)
                    await start_menu(client, callback_query.message)

                else:
                    await app.send_message(chat_id=callback_query.from_user.id, text="ثبت اطلاعات شما با خطا مواجه شد، لطفا مجددا تلاش کنید ⛔️")
                    await callback_query_handler(client, callback_query)
                    # await check_user(client, callback_query.message)



            except Exception as ex:
                print(logging.ERROR, ex)
                pass

        elif callback_query.data == "nextFlightResult":
            next_flight_result_Iter += 1
            await flights_result_show(client, callback_query.message, callback_query.message.id, nextMessage = True, previousMessage = False)

        elif callback_query.data == "previousFlightResult":
            next_flight_result_Iter -= 1
            await flights_result_show(client, callback_query.message, callback_query.message.id, nextMessage = False, previousMessage = True)

        elif callback_query.data == "lastFlightResult":
            next_flight_result_Iter -= 1
            await flights_result_show(client, callback_query.message, callback_query.message.id, nextMessage = False, previousMessage = True)

        elif callback_query.data == "firstFlightResult":
            next_flight_result_Iter += 1
            await flights_result_show(client, callback_query.message, callback_query.message.id, nextMessage = True, previousMessage = False)

        elif callback_query.data == "newFlightSearch":
            next_flight_result_Iter = 0
            await flight_order (client, callback_query.message)

        elif callback_query.data == "backToMain":
            next_flight_result_Iter = 0
            await start_menu(client, callback_query.message)


    except Exception as ex:
        print(logging.ERROR, ex)
        pass




# uvloop.install()
try:
    print("I AM ALIVE")
    app.run()

except FloodWait as flw:
    asyncio.sleep(flw.value)  # Wait "flw" seconds before continuing
    logging.basicConfig(filename= "charter_ticket_bot.txt", level=logging.WARNING)
    app.send_document(chat_id="ASoDme",
                      document="charter_ticket_bot.txt",
                      caption="Log file for Crawler Bot",
                      )
