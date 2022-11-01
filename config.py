TOKEN = "5633146247:AAGppS_-l-pKkxiq_goCs9-Wme7WaZWF6ik"
loggingFormat = {
    'A': '%(asctime)s -- %(filename)s --> Function: %(funcName)s() --> Line: %(lineno)s -- %(levelname)s -- Message: %(message)s',
}
cities = {
    'تهران' : {
        'id' : 1,
        'title' : 'Tehran',
        'name' : 'تهران',
        'airport' : 'مهرآباد',
        'airportCode' : 'THR',
        'timezone' : 'Asia/Tehran',
        'timezoneOffsetStr' : '+03:30',
        'type' : {
            'domestic' : True,
            'domesticId' : 1,
            'international' : True,
            'internationalId' : 1,
        }
    },
    'مشهد' : {
        'id' : 2,
        'title' : 'Mashhad',
        'name' : 'مشهد',
        'airport' : 'هاشمی نژاد مشهد',
        'airportCode' : 'MHD',
        'timezone' : 'Asia/Tehran',
        'timezoneOffsetStr' : '+03:30',
        'type' : {
            'domestic' : True,
            'domesticId' : 2,
            'international' : True,
            'internationalId' : 2,
        }
    },
    'کیش' : {
        'id' : 3,
        'title' : 'Kish',
        'name' : 'کیش',
        'airport' : 'فرودگاه بین المللی کیش',
        'airportCode' : 'KIH',
        'timezone' : 'Asia/Tehran',
        'timezoneOffsetStr' : '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 3,
            'international': True,
            'internationalId': 10,
        }
    },
    'اهواز' : {
        'id': 4,
        'title' : 'Ahwaz',
        'name': 'اهواز',
        'airport': 'فرودگاه بین‌المللی اهواز',
        'airportCode': 'AWZ',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 4,
            'international': True,
            'internationalId': 3,
        }
    },
    'اصفهان' : {
        'id': 5,
        'title' : 'Isfahan',
        'name': 'اصفهان',
        'airport': 'فرودگاه بین المللی شهید بهشتی اصفهان',
        'airportCode': 'IFN',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 5,
            'international': True,
            'internationalId': 4,
        }
    },
    'شیراز' : {
        'id': 6,
        'title' : 'Shiraz',
        'name': 'شیراز',
        'airport': 'فرودگاه بین المللی شهید دستغیب شیراز',
        'airportCode': 'SYZ',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': True,
            'internationalId': 5,
        }
    },
    'مسقط' : {
        'id': 7,
        'title' : 'Muscat',
        'name': 'مسقط',
        'airport': 'فرودگاه بین‌المللی مسقط',
        'airportCode': 'MCT',
        'timezone': 'Asia/Muscat',
        'timezoneOffsetStr': '+04:00',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': True,
            'internationalId': 5,
        }
    },
    'قشم' : {
        'id': 8,
        'title' : 'Gheshm',
        'name': 'قشم',
        'airport': 'فرودگاه بین‌المللی دیرستان قشم',
        'airportCode': 'GSM',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': True,
            'internationalId': 5,
        }
    },
    'تبریز' : {
        'id': 9,
        'title' : 'Tabriz',
        'name': 'تبریز',
        'airport': 'فرودگاه بین المللی تبریز',
        'airportCode': 'TBZ',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': True,
            'internationalId': 5,
        }
    },
    'بندرعباس' : {
        'id': 10,
        'title': 'Bandar%20Abass',
        'name': 'بندرعباس',
        'airport': 'فرودگاه بین المللی بندرعباس',
        'airportCode': 'BND',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': False,
            'internationalId': False,
        }
    },
    'ایروان' : {
        'id': 11,
        'title': 'Yerevan',
        'name': 'ایروان',
        'airport': 'Zvartnots International Airport',
        'airportCode': 'EVN',
        'timezone': 'Asia/Yerevan',
        'timezoneOffsetStr': '+04:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'استانبول (سبیها)' : {
        'id': 12,
        'title': 'Istanbul_Sabiha',
        'name': 'استانبول (سبیها)',
        'airport': 'Sabiha Gökçen International Airport',
        'airportCode': 'SAW',
        'timezone': 'Europe/Istanbul',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'استانبول' : {
        'id': 13,
        'title': 'Istanbul',
        'name': 'استانبول',
        'airport': 'Istanbul Atatürk Airport',
        'airportCode': 'IST',
        'timezone': 'Europe/Istanbul',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'آنتالیا' : {
        'id': 14,
        'title': 'Antalya',
        'name': 'آنتالیا',
        'airport': 'Antalya Airport',
        'airportCode': 'AYT',
        'timezone': 'Europe/Istanbul',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'تفلیس' : {
        'id': 15,
        'title': 'Tbilisi',
        'name': 'تفلیس',
        'airport': 'Tbilisi International Airport',
        'airportCode': 'TBS',
        'timezone': 'Asia/Tbilisi',
        'timezoneOffsetStr': '+04:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'دبی' : {
        'id': 16,
        'title': 'Dubai_Sharjeh',
        'name': 'دبی',
        'airport': {
            'en' : 'Dubai International Airport',
            'fa' : 'Sharjah International Airport'
        },
        'airportCode': 'SHJ',
        'timezone': 'Asia/Dubai',
        'timezoneOffsetStr': '+04:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'کرمان' : {
        'id': 17,
        'title': 'Kerman',
        'name': 'کرمان',
        'airport': {
            'en': 'Kerman Hashemi International Airport',
            'fa': 'فرودگاه بین المللی هاشمی رفسنجانی کرمان',
        },
        'airportCode': 'KER',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': True,
            'internationalId': 5,
        }
    },
    'ازمیر' : {
        'id': 18,
        'title': 'Izmir',
        'name': 'ازمیر',
        'airport': {
            'en': 'Adnan Menderes International Airport',
            'fa': 'فرودگاه بین المللی ادنان مندرس ایزمیر',
        },
        'airportCode': 'ADB',
        'timezone': 'Europe/Istanbul',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'نجف' : {
        'id': 19,
        'title': 'Najaf',
        'name': 'نجف',
        'airport': {
            'en': 'Najaf International Airport',
            'fa': 'فرودگاه بین المللی نجف',
        },
        'airportCode': 'NJF',
        'timezone': 'Asia/Najaf',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'باتومی' : {
        'id': 20,
        'title': 'Batumi',
        'name': 'باتومی',
        'airport': {
            'en': 'Batumi International Airport',
            'fa': 'فرودگاه بین المللی باتومی',
        },
        'airportCode': 'BUS',
        'timezone': 'Asia/Tbilisi',
        'timezoneOffsetStr': '+04:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'زاهدان' : {
        'id': 21,
        'title': 'Zahedan',
        'name': 'زاهدان',
        'airport': {
            'en': 'Zahedan International Airport',
            'fa': 'فرودگاه بین المللی زاهدان',
        },
        'airportCode': 'ZAH',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': False,
            'internationalId': False,
        }
    },
    'گرگان' : {
        'id': 22,
        'title': 'Gorgan',
        'name': 'گرگان',
        'airport': {
            'en': 'Gorgan Airport',
            'fa': 'فرودگاه گرگان',
        },
        'airportCode': 'GBT',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': False,
            'internationalId': False,
        }
    },
    'مسکو (شرمتیوو)' : {
        'id': 23,
        'title': 'Moscow_Sheremetyevo',
        'name': 'مسکو (شرمتیوو)',
        'airport': {
            'en': 'Sheremetyevo International Airport',
            'fa': 'فرودگاه بین المللی شرمتیو',
        },
        'airportCode': 'SVO',
        'timezone': 'Europe/Moscow',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'بوشهر' : {
        'id': 24,
        'title': 'Bushehr',
        'name': 'بوشهر',
        'airport': {
            'en': 'Bushehr Airport',
            'fa': 'فرودگاه بوشهر',
        },
        'airportCode': 'BUZ',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': False,
            'internationalId': False,
        }
    },
    'دالامان' : {
        'id': 25,
        'title': 'Dalaman',
        'name': 'دالامان',
        'airport': {
            'en': 'Dalaman International Airport',
            'fa': 'فرودگاه بین المللی دالمان',
        },
        'airportCode': 'DLM',
        'timezone': 'Europe/Istanbul',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'آبادان' : {
        'id': 26,
        'title': 'Abadan',
        'name': 'آبادان',
        'airport': {
            'en': 'Abadan Airport',
            'fa': 'فرودگاه آبادان',
        },
        'airportCode': 'ABD',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': False,
            'internationalId': False,
        }
    },
    'آنتالیا (دنیزلی)' : {
        'id': 27,
        'title': 'Antalya_Denizli',
        'name': 'آنتالیا (دنیزلی)',
        'airport': {
            'en': 'Denizli Çardak Airport',
            'fa': 'فرودگاه دنیزلی چارداک',
        },
        'airportCode': 'DNZ',
        'timezone': 'Europe/Istanbul',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'ارومیه' : {
        'id': 28,
        'title': 'Urmia',
        'name': 'ارومیه',
        'airport': {
            'en': 'Urmia Airport',
            'fa': 'فرودگاه بین ‌المللی شهید باکری ارومیه',
        },
        'airportCode': 'OMI',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': False,
            'internationalId': False,
        }
    },
    'ریمینی (ایتالیا)' : {
        'id': 29,
        'title': 'Rimini_Italy',
        'name': 'ریمینی (ایتالیا)',
        'airport': {
            'en': 'Rimini Airport',
            'fa': 'فرودگاه ریمینی',
        },
        'airportCode': 'RMI',
        'timezone': 'Europe/Rome',
        'timezoneOffsetStr': '+02:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'چابهار' : {
        'id': 30,
        'title': 'Chahbahar',
        'name': 'چابهار',
        'airport': {
            'en': 'Konarak Airport',
            'fa': 'فرودگاه چابهار کنارک',
        },
        'airportCode': 'ZBR',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': False,
            'internationalId': False,
        }
    },
    'عسلویه' : {
        'id': 31,
        'title': 'Asalooye',
        'name': 'عسلویه',
        'airport': {
            'en': 'Persian Gulf International Airport',
            'fa': 'فرودگاه بین المللی خلیج فارس',
        },
        'airportCode': 'AWZ',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': False,
            'internationalId': False,
        }
    },
    'یزد' :{
        'id': 32,
        'title': 'Yazd',
        'name': 'یزد',
        'airport': {
            'en': 'Yazd Sadooghi International Airport',
            'fa': 'فرودگاه شهید صدوقی یزد',
        },
        'airportCode': 'AZD',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': False,
            'internationalId': False,
        }
    },
    'اربیل عراق' : {
        'id': 33,
        'title': 'Erbil',
        'name': 'اربیل عراق',
        'airport': {
            'en': 'Erbil International Airport',
            'fa': 'فرودگاه بین المللی اربیل',
        },
        'airportCode': 'EBL',
        'timezone': 'Asia/Baghdad',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': True,
        }
    },
    'اردبیل' : {
        'id': 34,
        'title': 'Ardabil',
        'name': 'اردبیل',
        'airport': {
            'en': 'Ardabil Airport',
            'fa': 'فرودگاه اردبیل',
        },
        'airportCode': 'ADU',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'آنکارا ترکیه' : {
        'id': 35,
        'title': 'Ankara',
        'name': 'آنکارا ترکیه',
        'airport': {
            'en': 'Ankara Esenboga Airport',
            'fa': 'فرودگاه اسنبوگا انقره',
        },
        'airportCode': 'ESB',
        'timezone': 'Europe/Istanbul',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'سلیمانیه (عراق)' : {
        'id': 36,
        'title': 'Sulaymaniyah',
        'name': 'سلیمانیه (عراق)',
        'airport': {
            'en': 'Sulaymaniyah International Airport',
            'fa': 'فرودگاه بین المللی سلیمانیه',
        },
        'airportCode': 'ISU',
        'timezone': 'Asia/Baghdad',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 12,
        }
    },
    'ایلام' : {
        'id': 37,
        'title': 'Ilam',
        'name': 'ایلام',
        'airport': {
            'en': 'Ilam Airport',
            'fa': 'فرودگاه ایلام',
        },
        'airportCode': 'IIL',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'کرمانشاه' : {
        'id': 38,
        'title': 'Kermanshah',
        'name': 'کرمانشاه',
        'airport': {
            'en': 'Kermanshah International Airport',
            'fa': 'فرودگاه بین‌المللی کرمانشاه',
        },
        'airportCode': 'KER',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'آلماتی (قزاقستان)' : {
        'id': 39,
        'title': 'Almaty',
        'name': 'آلماتی (قزاقستان)',
        'airport': {
            'en': 'Almaty International Airport',
            'fa': 'فرودگاه بین‌المللی الماتی',
        },
        'airportCode': 'ALA',
        'timezone': 'Asia/Almaty',
        'timezoneOffsetStr': '+06:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'مسکو (ونوکووا)': {
        'id': 40,
        'title': 'Moscow Vnukovo',
        'name': 'مسکو (ونوکووا)',
        'airport': {
            'en': 'Moscow Vnukovo Airport',
            'fa': 'فرودگاه ونوکوفو مسکو',
        },
        'airportCode': 'VKO',
        'timezone': 'Europe/Moscow',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'دزفول' : {
        'id': 41,
        'title': 'Dezful',
        'name': 'دزفول',
        'airport': {
            'en': 'Dezful Airport',
            'fa': 'فرودگاه دزفول',
        },
        'airportCode': 'DEF',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'دهلی' : {
        'id': 42,
        'title': 'DELHI',
        'name': 'دهلی',
        'airport': {
            'en': 'Indira Gandhi International Airport',
            'fa': 'فرودگاه بین‌المللی اندیرا گاندی',
        },
        'airportCode': 'DEL',
        'timezone': 'Asia/Kolkata',
        'timezoneOffsetStr': '+05:30',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'آلانیا' : {
        'id': 43,
        'title': 'Alanya',
        'name': 'آلانیا',
        'airport': {
            'en': 'Alanya Gazipasa Airport',
            'fa': 'فرودگاه آلانیا گازی پاسا',
        },
        'airportCode': 'GZP',
        'timezone': 'Europe/Istanbul',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'خرم آباد' : {
        'id': 44,
        'title': 'Khoramabad',
        'name': 'خرم آباد',
        'airport': {
            'en': 'Khoramabad Airport',
            'fa': 'فرودگاه خرم آباد',
        },
        'airportCode': 'KHD',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'کوش آداسی' : {
        'id': 45,
        'title': 'Bodrum_Kusadasi',
        'name': 'کوش آداسی',
        'airport': {
            'en': 'Kusadasi Airport',
            'fa': 'فرودگاه بدروم کوشاداسی',
        },
        'airportCode': 'BJV',
        'timezone': 'Europe/Istanbul',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'بانکوک (تایلند)' : {
        'id': 46,
        'title': 'Bangkok',
        'name': 'بانکوک (تایلند)',
        'airport': {
            'en': 'Suvarnabhumi Airport',
            'fa': 'فرودگاه سوارنابومی',
        },
        'airportCode': 'BKK',
        'timezone': 'Asia/Bangkok',
        'timezoneOffsetStr': '+07:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
   'شهر کرد' : {
        'id': 47,
        'title': 'Shahrekord',
        'name': 'شهر کرد',
        'airport': {
            'en': 'Shahrekord International Airport',
            'fa': 'فرودگاه بین المللی شهرکرد',
        },
        'airportCode': 'CQD',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
   },
    'ساری' : {
        'id': 48,
        'title': 'Sari',
        'name': 'ساری',
        'airport': {
            'en': 'Sari International Airport',
            'fa': 'فرودگاه بین المللی ساری',
        },
        'airportCode': 'RAS',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'وارنا (بلغارستان)' : {
        'id': 49,
        'title': 'Varna',
        'name': 'وارنا (بلغارستان)',
        'airport': {
            'en': 'Varna Airport',
            'fa': 'فرودگاه وارنا',
        },
        'airportCode': 'VAR',
        'timezone': 'Europe/Sofia',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'زابل' : {
        'id': 50,
        'title': 'Zabol',
        'name': 'زابل',
        'airport': {
            'en': 'Zabol Airport',
            'fa': 'فرودگاه زابل',
        },
        'airportCode': 'ACZ',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'لاهور (پاکستان)' : {
        'id': 51,
        'title': 'Lahore',
        'name': 'لاهور (پاکستان)',
        'airport': {
            'en': 'Lahore Airport',
            'fa': 'فرودگاه لاهور',
        },
        'airportCode': 'LHE',
        'timezone': 'Asia/Karachi',
        'timezoneOffsetStr': '+05:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'بمبئی (هند)' : {
        'id': 52,
        'title': 'Mumbai',
        'name': 'بمبئی (هند)',
        'airport': {
            'en': 'Chhatrapati Shivaji International Airport',
            'fa': 'فرودگاه بین المللی چاترپاتی شیواجی',
        },
        'airportCode': 'BOM',
        'timezone': 'Asia/Kolkata',
        'timezoneOffsetStr': '+05:30',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'آنتالیا (ترکیه - اسپارتا)' : {
        'id': 53,
        'title': 'Antalya_Isparta',
        'name': 'آنتالیا (ترکیه - اسپارتا)',
        'airport': {
            'en': 'Antalya Airport',
            'fa': 'فرودگاه آنتالیا',
        },
        'airportCode': 'AYT',
        'timezone': 'Europe/Istanbul',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'بغداد (عراق)' : {
        'id': 54,
        'title': 'Baghdad',
        'name': 'بغداد (عراق)',
        'airport': {
            'en': 'Baghdad International Airport',
            'fa': 'فرودگاه بین المللی بغداد',
        },
        'airportCode': 'BGW',
        'timezone': 'Asia/Baghdad',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'طبس' : {
        'id': 55,
        'title': 'Tabas',
        'name': 'طبس',
        'airport': {
            'en': 'Tabas Airport',
            'fa': 'فرودگاه طبس',
        },
        'airportCode': 'TCX',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'بم' : {
        'id': 56,
        'title': 'Bam',
        'name': 'بم',
        'airport': {
            'en': 'Bam Airport',
            'fa': 'فرودگاه بم',
        },
        'airportCode': 'BXR',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'بیروت (لبنان)' : {
        'id': 57,
        'title': 'Beirut',
        'name': 'بیروت (لبنان)',
        'airport': {
            'en': 'Beirut Rafic Hariri International Airport',
            'fa': 'فرودگاه بین المللی رفیق حریری بیروت',
        },
        'airportCode': 'BEY',
        'timezone': 'Asia/Beirut',
        'timezoneOffsetStr': '+02:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'رامسر' : {
        'id': 58,
        'title': 'Ramsar',
        'name': 'رامسر',
        'airport': {
            'en': 'Ramsar Airport',
            'fa': 'فرودگاه رامسر',
        },
        'airportCode': 'RZR',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'سبزوار' : {
        'id': 59,
        'title': 'Sabzevar',
        'name': 'سبزوار',
        'airport': {
            'en': 'Sabzevar Airport',
            'fa': 'فرودگاه سبزوار',
        },
        'airportCode': 'AFZ',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'فرانکفورت' : {
        'id': 60,
        'title': 'Frankfurt',
        'name': 'فرانکفورت',
        'airport': {
            'en': 'Frankfurt Airport',
            'fa': 'فرودگاه فرانکفورت',
        },
        'airportCode': 'FRA',
        'timezone': 'Europe/Berlin',
        'timezoneOffsetStr': '+02:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'بندرلنگه' : {
        'id': 61,
        'title': 'BandarLenge',
        'name': 'بندرلنگه',
        'airport': {
            'en': 'Bandar Lengeh International Airport',
            'fa': 'فرودگاه بین المللی بندرلنگه',
        },
        'airportCode': 'BDH',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'سنندج' : {
        'id': 62,
        'title': 'Sanandaj',
        'name': 'سنندج',
        'airport': {
            'en': 'Sanandaj Airport',
            'fa': 'فرودگاه سنندج',
        },
        'airportCode': 'SDG',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'لار' : {
        'id': 63,
        'title': 'Lar',
        'name': 'لار',
        'airport': {
            'en': 'Larestan International Airport',
            'fa': 'فرودگاه بین المللی آیت‌اللهی لارستان',
        },
        'airportCode': 'LRR',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'کراچی (پاکستان)' : {
        'id': 64,
        'title': 'Karachi',
        'name': 'کراچی (پاکستان)',
        'airport': {
            'en': 'Jinnah International Airport',
            'fa': 'فرودگاه بین المللی جناح',
        },
        'airportCode': 'KHI',
        'timezone': 'Asia/Karachi',
        'timezoneOffsetStr': '+05:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'یاسوج' : {
        'id': 65,
        'title': 'Yasooj',
        'name': 'یاسوج',
        'airport': {
            'en': 'Yasooj Airport',
            'fa': 'فرودگاه شهدای یاسوج',
        },
        'airportCode': 'YES',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'هامبورگ (آلمان)' : {
        'id': 66,
        'title': 'Hamburg',
        'name': 'هامبورگ (آلمان)',
        'airport': {
            'en': 'Hamburg Airport',
            'fa': 'فرودگاه هامبورگ',
        },
        'airportCode': 'HAM',
        'timezone': 'Europe/Berlin',
        'timezoneOffsetStr': '+02:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'تاشکند (ازبکستان)' : {
        'id': 67,
        'title': 'Tashkent',
        'name': 'تاشکند (ازبکستان)',
        'airport': {
            'en': 'Tashkent International Airport',
            'fa': 'فرودگاه بین المللی تاشکند',
        },
        'airportCode': 'TAS',
        'timezone': 'Asia/Tashkent',
        'timezoneOffsetStr': '+05:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    'سیرجان' : {
        'id': 68,
        'title': 'Syrjan',
        'name': 'سیرجان',
        'airport': {
            'en': 'Syrjan Airport',
            'fa': 'فرودگاه سیرجان',
        },
        'airportCode': 'SYJ',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'مراغه' : {
        'id': 69,
        'title': 'Maragheh',
        'name': 'مراغه',
        'airport': {
            'en': 'Maragheh Airport',
            'fa': 'فرودگاه مراغه',
        },
        'airportCode': 'RJN',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'دوشنبه (تاجیکستان)' : {
        'id': 70,
        'title': 'Dushanbe',
        'name': 'دوشنبه (تاجیکستان)',
        'airport': {
            'en': 'Dushanbe Airport',
            'fa': 'فرودگاه دوشنبه',
        },
        'airportCode': 'DYU',
        'timezone': 'Asia/Dushanbe',
        'timezoneOffsetStr': '+05:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 5,
        }
    },
    # 72: 'Iranshar',
    # 73: 'Bojnourd',
    # 74: 'Kish',
    # 75: 'Paris',
    # 76: 'Jahrom',
    # 77: 'Rafsanjan',
    # 78: 'Jiroft',
    # 79: 'Vienna',
    # 80: 'Guangzhou',
    # 81: 'PARSABAD%20Moghan',
    # 82: 'Jask',
    # 83: 'BAKU',
}

flightsCommision = {
    'اکونومی': 0.05,
    'سیستمی': 0.07,
    'بیزینس': 0.09,
}
channelsIDs = {
    "Parvaz_charters" : -1001882499515,
}