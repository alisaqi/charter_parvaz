# coding=utf8

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from charterTicket import flights_handler
from persiantools.jdatetime import JalaliDate
from pyrogram import Client, filters
import logging
import datetime
import pytz
import config


app = Client("Charter_ticketbot",
             api_id=14244400,
             api_hash="118639cb7a29cf67eb5e45a4251a8aa4",
             bot_token= "5633146247:AAGppS_-l-pKkxiq_goCs9-Wme7WaZWF6ik"
             )


users_db = {}
flights_result = {}
flight_date = 0
destination_city = None
departure_city = None
next_flight_result_iter = 0

def jalali_dates(today):
    dates = {}
    i = 0
    while i < 30:
        dates[i] = (JalaliDate(today) + datetime.timedelta(days=i)).isoformat()
        i += 1
    return dates


@app.on_message(filters.command('start') & filters.private)
async def pre_check_user(client, message):
    global users_db
    try:
        if message.from_user.id not in users_db.keys():
            await app.send_message(
                chat_id=message.chat.id,
                text='سلام به ربات Flight Charter خوش آمدید\n\n⚠️ شما هنوز عضو کانال ما نشدین، لطفا جهت ادامه فعالیت روی دکمه زیر کلیک کنید.',
                reply_markup=InlineKeyboardMarkup(
                    [
                        [  # First row
                            InlineKeyboardButton(  # Opens a web URL
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

    except Exception as ex:
        print(logging.ERROR, ex)
        pass

@app.on_message(filters.private)
async def start_menu(client, message):
    try:
        answer = await app.ask(
            chat_id=message.chat.id,
            text='لطفا یکی از خدمات زیر را انتخاب کنید:',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ["بلیط هواپیما ✈️"],
                    ["بلیط اتوبوس 🚌"],
                    ["ارتباط با ما 📩"],
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            ))

        if answer.text == "بلیط هواپیما ✈️":
            await flight_order(client, message)
        # elif answer.text == "محاسبه قیمت لحظه ای 💸":
            # await serviceFeePriceCalculator(client, message)

    except Exception as ex:
        print(logging.ERROR, ex)
        pass

@app.on_message(filters.private)
async def flight_order (client, message):
    try:
        answer = await app.ask(
            chat_id=message.chat.id,
            text='لطفا نوع پرواز خود را انتخاب کنید:',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ["پرواز داخلی 🇮🇷"],
                    ["پرواز خارجی 🌍"],
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            ))

        if answer.text == "پرواز داخلی 🇮🇷":
            await domestic_flights_order(client, message)
        # elif answer.text == "محاسبه قیمت لحظه ای 💸":
            # await serviceFeePriceCalculator(client, message)

    except Exception as ex:
        print(logging.ERROR, ex)
        pass

# @app.on_inline_query()
# async def inline_query(client, inline_query):
#     for inline_result in config.cities.values():
#         await inline_query.answer(
#             results=[
#                 InlineQueryResultArticle(
#                     title= inline_result['name'],
#                     description= inline_result['title'],
#                     input_message_content=InputTextMessageContent(
#                         inline_result['name']
#                     )
#                 )
#             ],
#             cache_time=1
#         )

@app.on_message(filters.private)
async def domestic_flights_order (client, message):
    global flights_result
    global flight_date
    global departure_city
    global destination_city

    try:
        departure_city = await app.ask (
            chat_id=message.chat.id,
            text='لطفا مبدا خود را انتخاب کنید:',
            # reply_markup=ReplyKeyboardMarkup()
            reply_markup=ReplyKeyboardMarkup(
                [
                    [cities] for cities in config.cities.keys()
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        destination_city = await app.ask(
            chat_id=message.chat.id,
            text='لطفا مقصد خود را انتخاب کنید:',
            reply_markup=ReplyKeyboardMarkup(
                [
                    [dates] for dates in config.cities.keys()
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        flight_date = await app.ask (
            chat_id=message.chat.id,
            text='لطفا تاریخ سفر خود را انتخاب کنید:',
            reply_markup=ReplyKeyboardMarkup(
                [
                    [dates] for dates in jalali_dates(JalaliDate.today()).values()
                ],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

        previous_message = await app.send_message(
            chat_id=message.chat.id,
            text="ربات در حال گرفتن اطلاعات پرواز ها می باشد 🚀"
        )

        flights_result = flights_handler(departure_city= config.cities[departure_city.text]['title'],
                                         destination_city= config.cities[destination_city.text]['title'],
                                         flight_date= flight_date.text)

        # print(flightsResult)
        await flights_result_show(client, message, previous_message.id, nextMessage= True, previousMessage= False)


    except Exception as ex:
        print(logging.ERROR, ex)
        pass

@app.on_message(filters.private)
async def flights_result_show (client, message, previous_message_id, nextMessage, previousMessage):
    global next_flight_result_iter
    global flights_result
    global flight_date
    global destination_city
    global departure_city

    try:
        if flights_result != False:
            commission = config.flightsCommision[flights_result[next_flight_result_iter]['ticketType']] + 1
            lastResultId = list(flights_result.keys())[-1]
            firstResultId = list(flights_result.keys())[0]
            purchaseUrl = 'https://t.me/ASoDme'
            # purchaseUrl = 'http://ticket-charter.com/Ticket' + '-' + config.cities[departureCity.text]['title'] + '-' + config.cities[destinationCity.text]['title'] + '.html' + '?' + 't='  + flightDate.text
            finalText = f"پرواز {departure_city.text} 🛫 به {destination_city.text} 🛬\n\n✈️ شماره پرواز : {flights_result[next_flight_result_iter]['flightNumber']}\n\n🎫 نوع بلیط : {flights_result[next_flight_result_iter]['ticketType']}\n\n💵 قیمت : {int(float(flights_result[next_flight_result_iter]['priceDigit'] * commission)):,} تومان\n\n📅 تاریخ و ساعت پرواز: \n{flight_date.text}\n{flights_result[next_flight_result_iter]['departure']}\n💺 تعداد صندلی خالی: {flights_result[next_flight_result_iter]['freeSeats']}\n\n🌐 هواپیمایی: {flights_result[next_flight_result_iter]['company']}"


            if previousMessage == False and nextMessage == True and list(flights_result.keys())[next_flight_result_iter] == (firstResultId) and len(flights_result.keys()) > 1:
                await app.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=previous_message_id,
                    text=finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url=purchaseUrl
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
                                    "بازگشت به منو اصلی 🔙",
                                    callback_data="backToMain"
                                )
                            ],

                        ]

                    )
                )
            elif previousMessage == False and nextMessage == True and list(flights_result.keys())[next_flight_result_iter] == (firstResultId) and len(flights_result.keys()) == 1:
                await app.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=previous_message_id,
                    text=finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url=purchaseUrl
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
                                    "بازگشت به منو اصلی 🔙",
                                    callback_data="backToMain"
                                )
                            ],

                        ]

                    )
                )
            elif previousMessage == True and nextMessage == False and list(flights_result.keys())[next_flight_result_iter] == (lastResultId):
                await app.edit_message_text(
                    chat_id = message.chat.id,
                    message_id = previous_message_id,
                    text= finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url= purchaseUrl
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
                                    "بازگشت به منو اصلی 🔙",
                                    callback_data="backToMain"
                                )
                            ]
                        ]
                    )
                )
            elif previousMessage == False and nextMessage == True and list(flights_result.keys())[next_flight_result_iter] != firstResultId and list(flights_result.keys())[next_flight_result_iter] != lastResultId:
                await app.edit_message_text(
                    chat_id = message.chat.id,
                    message_id = previous_message_id,
                    text=finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url= purchaseUrl
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
                                    "بازگشت به منو اصلی 🔙",
                                    callback_data="backToMain"
                                )
                            ]
                        ]
                    )
                )
            elif previousMessage == False and nextMessage == True and list(flights_result.keys())[next_flight_result_iter] != firstResultId and list(flights_result.keys())[next_flight_result_iter] == lastResultId:

                await app.edit_message_text(
                    chat_id = message.chat.id,
                    message_id = previous_message_id,
                    text=finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url= purchaseUrl
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
                                    "بازگشت به منو اصلی 🔙",
                                    callback_data="backToMain"
                                )
                            ]
                        ]
                    )
                )
            elif previousMessage == True and nextMessage == False and list(flights_result.keys())[next_flight_result_iter] != firstResultId and list(flights_result.keys())[next_flight_result_iter] != lastResultId:
                await app.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=previous_message_id,
                    text=finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url= purchaseUrl
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
                                    "بازگشت به منو اصلی 🔙",
                                    callback_data="backToMain"
                                )
                            ]
                        ]
                    )
                )
            elif previousMessage == True and nextMessage == False and list(flights_result.keys())[next_flight_result_iter] == firstResultId and list(flights_result.keys())[next_flight_result_iter] != lastResultId:
                await app.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=previous_message_id,
                    text=finalText,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "خرید این بلیط 🛒",
                                    url= purchaseUrl
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
                                    "بازگشت به منو اصلی 🔙",
                                    callback_data="backToMain"
                                )
                            ]
                        ]
                    )
                )

        elif flights_result == False:
            await app.edit_message_text(
                chat_id=message.chat.id,
                message_id=previous_message_id,
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
                                "بازگشت به منو اصلی 🔙",
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
    global next_flight_result_iter

    try:
        if callback_query.data == "membershipApproval":
            async for members in app.get_chat_members(chat_id=config.channelsIDs["Parvaz_charters"]):
                if members.user.id == callback_query.from_user.id:
                    foundUser = True
                    users_db[callback_query.from_user.id] = {
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

        elif callback_query.data == "nextFlightResult":
            next_flight_result_iter += 1
            await flights_result_show(client, callback_query.message, callback_query.message.id, nextMessage = True, previousMessage = False)

        elif callback_query.data == "previousFlightResult":
            next_flight_result_iter -= 1
            await flights_result_show(client, callback_query.message, callback_query.message.id, nextMessage = False, previousMessage = True)

        elif callback_query.data == "lastFlightResult":
            next_flight_result_iter -= 1
            await flights_result_show(client, callback_query.message, callback_query.message.id, nextMessage = False, previousMessage = True)

        elif callback_query.data == "firstFlightResult":
            next_flight_result_iter += 1
            await flights_result_show(client, callback_query.message, callback_query.message.id, nextMessage = True, previousMessage = False)

        elif callback_query.data == "newFlightSearch":
            await flight_order (client, callback_query.message)

        elif callback_query.data == "backToMain":
            await start_menu(client, callback_query.message)


    except Exception as ex:
        print(logging.ERROR, ex)
        pass




# uvloop.install()
print("I AM ALIVE")
app.run()