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
    'Gorgan' : {
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
    'Abadan' : {
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
    'Kermanshah' : {
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
    'Moscow_Vnukovo': {
        'id': 40,
        'title': 'Moscow Vnukovo',
        'name': 'مسکو (ونوکوفو)',
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
    # 41: 'Dezful',
    # 42: 'DELHI',
    # 43: 'Alanya',
    # 44: 'Khoramabad',
    # 45: 'Bodrum_Kusadasi',
    # 46: 'Bangkok',
    # 47: 'Shahrekord',
    # 48: 'Sari',
    # 49: 'Varna',
    # 50: 'Zabol',
    # 51: 'Lahore',
    # 52: 'Mumbai',
    # 53: 'Antalya_Isparta',
    # 54: 'Baghdad',
    # 55: 'Tabas',
    # 56: 'Bam',
    # 57: 'Beirut',
    # 58: 'Gheshm',
    # 59: 'Ramsar',
    # 60: 'Sabzevar',
    # 61: 'Frankfurt',
    # 62: 'BandarLenge',
    # 63: 'Sanandaj',
    # 64: 'Lar',
    # 65: 'Karachi',
    # 66: 'Yasooj',
    # 67: 'Hamburg',
    # 68: 'Tashkent',
    # 69: 'Syrjan',
    # 70: 'Maragheh',
    # 71: 'Dushanbe',
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