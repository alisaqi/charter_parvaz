import os
import re

# Bot credentials - should be set via environment variables
API_ID = int(os.getenv('TELEGRAM_API_ID', '0'))
API_HASH = os.getenv('TELEGRAM_API_HASH', '')
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')

# Logging configuration
LOGGING_FORMAT = '%(asctime)s -- %(filename)s --> Function: %(funcName)s() --> Line: %(lineno)s -- %(levelname)s -- Message: %(message)s'
LOG_FILE = 'CHARTER_TICKETS_LOGS.txt'

# URL configuration
TICKET_BASE_URL = 'http://ticket-charter.com/Ticket'
CONTACT_URL = 'https://t.me/ASoDme'

# Input validation patterns
PERSIAN_NAME_PATTERN = re.compile(r'^[\u0600-\u06FF\s]+$')
ENGLISH_NAME_PATTERN = re.compile(r'^[a-zA-Z\s]+$')
PHONE_PATTERN = re.compile(r'^09\d{9}$')
NATIONAL_ID_PATTERN = re.compile(r'^\d{10}$')
PASSPORT_PATTERN = re.compile(r'^[A-Z0-9]{1,9}$|^0$')


def validate_persian_name(name):
    """Validate Persian name input."""
    return bool(name and PERSIAN_NAME_PATTERN.match(name.strip()))


def validate_english_name(name):
    """Validate English name input."""
    return bool(name and ENGLISH_NAME_PATTERN.match(name.strip()))


def validate_phone_number(phone):
    """Validate Iranian phone number."""
    return bool(phone and PHONE_PATTERN.match(phone.strip().replace(' ', '')))


def validate_national_id(national_id):
    """Validate Iranian national ID."""
    return bool(national_id and NATIONAL_ID_PATTERN.match(national_id.strip()))


def validate_passport(passport):
    """Validate passport number or 0 for no passport."""
    return bool(passport and PASSPORT_PATTERN.match(passport.strip().upper()))
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
    'اصفهان': {
        'id': 5,
        'title': 'Isfahan',
        'name': 'اصفهان',
        'airport': 'فرودگاه بین المللی شهید بهشتی اصفهان',
        'airportCode': 'IFN',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 4,
            'international': True,
            'internationalId': 3,
        }
    },
    'شیراز': {
        'id': 6,
        'title': 'Shiraz',
        'name': 'شیراز',
        'airport': 'فرودگاه بین المللی شهید دستغیب شیراز',
        'airportCode': 'SYZ',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 5,
            'international': True,
            'internationalId': 4,
        }
    },
    'اهواز': {
        'id': 4,
        'title': 'Ahwaz',
        'name': 'اهواز',
        'airport': 'فرودگاه بین‌المللی اهواز',
        'airportCode': 'AWZ',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 6,
            'international': True,
            'internationalId': 1,
        }
    },
    'تبریز': {
        'id': 9,
        'title': 'Tabriz',
        'name': 'تبریز',
        'airport': 'فرودگاه بین المللی تبریز',
        'airportCode': 'TBZ',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 7,
            'international': True,
            'internationalId': 5,
        }
    },
    'یزد': {
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
            'domesticId': 8,
            'international': False,
            'internationalId': False,
        }
    },
    'قشم': {
        'id': 8,
        'title': 'Gheshm',
        'name': 'قشم',
        'airport': 'فرودگاه بین‌المللی دیرستان قشم',
        'airportCode': 'GSM',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 9,
            'international': True,
            'internationalId': 5,
        }
    },
    'ارومیه': {
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
            'domesticId': 10,
            'international': False,
            'internationalId': False,
        }
    },
    'چابهار': {
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
            'domesticId': 11,
            'international': False,
            'internationalId': False,
        }
    },
    'بندرعباس': {
        'id': 10,
        'title': 'Bandar%20Abass',
        'name': 'بندرعباس',
        'airport': 'فرودگاه بین المللی بندرعباس',
        'airportCode': 'BND',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 12,
            'international': False,
            'internationalId': False,
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
            'domesticId': 13,
            'international': False,
            'internationalId': False,
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
            'domesticId': 14,
            'international': True,
            'internationalId': 5,
        }
    },
    'کرمانشاه': {
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
            'domesticId': 15,
            'international': False,
            'internationalId': False,
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
            'domesticId': 16,
            'international': False,
            'internationalId': False,
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
            'domesticId': 17,
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
            'domesticId': 18,
            'international': False,
            'internationalId': False,
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
            'domesticId': 19,
            'international': False,
            'internationalId': False,
        }
    },
    'خرم آباد': {
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
            'domesticId': 20,
            'international': False,
            'internationalId': False,
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
            'domesticId': 21,
            'international': False,
            'internationalId': False,
        }
    },
    'عسلویه': {
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
            'domesticId': 22,
            'international': False,
            'internationalId': False,
        }
    },
    'اردبیل': {
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
            'domesticId': 23,
            'international': False,
            'internationalId': False,
        }
    },
    'شهر کرد': {
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
            'domesticId': 24,
            'international': False,
            'internationalId': False,
        }
    },
    'ساری': {
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
            'domesticId': 25,
            'international': False,
            'internationalId': False,
        }
    },
    'زابل': {
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
            'domesticId': 26,
            'international': False,
            'internationalId': False,
        }
    },
    'طبس': {
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
            'domesticId': 27,
            'international': False,
            'internationalId': False,
        }
    },
    'بم': {
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
            'domesticId': 28,
            'international': False,
            'internationalId': False,
        }
    },
    'رامسر': {
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
            'domesticId': 29,
            'international': False,
            'internationalId': False,
        }
    },
    'سبزوار': {
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
            'domesticId': 30,
            'international': False,
            'internationalId': False,
        }
    },
    'بندرلنگه': {
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
            'domesticId': 31,
            'international': False,
            'internationalId': False,
        }
    },
    'سنندج': {
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
            'domesticId': 32,
            'international': False,
            'internationalId': False,
        }
    },
    'لار': {
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
            'domesticId': 33,
            'international': False,
            'internationalId': False,
        }
    },
    'یاسوج': {
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
            'domesticId': 34,
            'international': False,
            'internationalId': False,
        }
    },
    'سیرجان': {
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
            'domesticId': 35,
            'international': False,
            'internationalId': False,
        }
    },
    'مراغه': {
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
            'domesticId': 36,
            'international': False,
            'internationalId': False,
        }
    },
    'ایرانشهر': {
        'id': 71,
        'title': 'Iranshar',
        'name': 'ایرانشهر',
        'airport': {
            'en': 'Iranshar Airport',
            'fa': 'فرودگاه ایرانشهر',
        },
        'airportCode': 'IHR',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 37,
            'international': False,
            'internationalId': False,
        }
    },
    'بجنورد': {
        'id': 72,
        'title': 'Bojnourd',
        'name': 'بجنورد',
        'airport': {
            'en': 'Bojnurd International Airport',
            'fa': 'فرودگاه بین المللی بجنورد',
        },
        'airportCode': 'BJB',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 38,
            'international': False,
            'internationalId': False,
        }
    },
    'جهرم': {
        'id': 74,
        'title': 'Jahrom',
        'name': 'جهرم',
        'airport': {
            'en': 'Jahrom International Airport',
            'fa': 'فرودگاه بین المللی شهدای جهرم',
        },
        'airportCode': 'JAR',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 39,
            'international': False,
            'internationalId': False,
        }
    },
    'رفسنجان': {
        'id': 75,
        'title': 'Rafsanjan',
        'name': 'رفسنجان',
        'airport': {
            'en': 'Rafsanjan Airport',
            'fa': 'فرودگاه رفسنجان',
        },
        'airportCode': 'RJN',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 40,
            'international': False,
            'internationalId': False,
        }
    },
    'جیرفت': {
        'id': 76,
        'title': 'Jiroft',
        'name': 'جیرفت',
        'airport': {
            'en': 'Jiroft Airport',
            'fa': 'فرودگاه جیرفت',
        },
        'airportCode': 'JYR',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 41,
            'international': False,
            'internationalId': False,
        }
    },
    'پارس آباد مغان': {
        'id': 79,
        'title': 'Parsabad Moghan',
        'name': 'پارس آباد مغان',
        'airport': {
            'en': 'East Azerbaijan Airport',
            'fa': 'فرودگاه شهدای پارس‌آباد',
        },
        'airportCode': 'PFQ',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 42,
            'international': False,
            'internationalId': False,
        }
    },
    'جاسک': {
        'id': 80,
        'title': 'Jask',
        'name': 'جاسک',
        'airport': {
            'en': 'Jask Airport',
            'fa': 'فرودگاه شهدای هفتم آذر جاسک',
        },
        'airportCode': 'JSK',
        'timezone': 'Asia/Tehran',
        'timezoneOffsetStr': '+03:30',
        'type': {
            'domestic': True,
            'domesticId': 43,
            'international': False,
            'internationalId': False,
        }
    },

    'استانبول 🇹🇷': {
        'id': 13,
        'title': 'Istanbul',
        'name': 'استانبول 🇹🇷',
        'airport': 'Istanbul Atatürk Airport',
        'airportCode': 'IST',
        'timezone': 'Europe/Istanbul',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 6,
        }
    },
    'استانبول (سبیها) 🇹🇷': {
        'id': 12,
        'title': 'Istanbul_Sabiha',
        'name': 'استانبول (سبیها) 🇹🇷',
        'airport': 'Sabiha Gökçen International Airport',
        'airportCode': 'SAW',
        'timezone': 'Europe/Istanbul',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 7,
        }
    },
    'آنتالیا 🇹🇷': {
        'id': 14,
        'title': 'Antalya',
        'name': 'آنتالیا 🇹🇷',
        'airport': 'Antalya Airport',
        'airportCode': 'AYT',
        'timezone': 'Europe/Istanbul',
        'timezoneOffsetStr': '+03:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 8,
        }
    },
    'آنکارا 🇹🇷': {
        'id': 35,
        'title': 'Ankara',
        'name': 'آنکارا 🇹🇷',
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
            'internationalId': 9,
        }
    },
    'آلانیا 🇹🇷': {
        'id': 43,
        'title': 'Alanya',
        'name': 'آلانیا 🇹🇷',
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
            'internationalId': 10,
        }
    },
    'دبی 🇦🇪': {
        'id': 16,
        'title': 'Dubai_Sharjeh',
        'name': 'دبی 🇦🇪',
        'airport': {
            'en': 'Dubai International Airport',
            'fa': 'Sharjah International Airport'
        },
        'airportCode': 'SHJ',
        'timezone': 'Asia/Dubai',
        'timezoneOffsetStr': '+04:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 11,
        }
    },
    'تفلیس 🇬🇪': {
        'id': 15,
        'title': 'Tbilisi',
        'name': 'تفلیس 🇬🇪',
        'airport': 'Tbilisi International Airport',
        'airportCode': 'TBS',
        'timezone': 'Asia/Tbilisi',
        'timezoneOffsetStr': '+04:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 12,
        }
    },
    'ازمیر 🇹🇷': {
        'id': 18,
        'title': 'Izmir',
        'name': 'ازمیر 🇹🇷',
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
            'internationalId': 13,
        }
    },
    'آنتالیا (دنیزلی) 🇹🇷': {
        'id': 27,
        'title': 'Antalya_Denizli',
        'name': 'آنتالیا (دنیزلی) 🇹🇷',
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
            'internationalId': 14,
        }
    },
    'کوش آداسی 🇹🇷': {
        'id': 45,
        'title': 'Bodrum_Kusadasi',
        'name': 'کوش آداسی 🇹🇷',
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
            'internationalId': 15,
        }
    },
    'آنتالیا (ترکیه - اسپارتا) 🇹🇷': {
        'id': 53,
        'title': 'Antalya_Isparta',
        'name': 'آنتالیا (ترکیه - اسپارتا) 🇹🇷',
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
            'internationalId': 16,
        }
    },
    'دالامان 🇹🇷': {
        'id': 25,
        'title': 'Dalaman',
        'name': 'دالامان 🇹🇷',
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
            'internationalId': 17,
        }
    },
    'باتومی 🇬🇪': {
        'id': 20,
        'title': 'Batumi',
        'name': 'باتومی 🇬🇪',
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
            'internationalId': 18,
        }
    },
    'نجف 🇮🇶': {
        'id': 19,
        'title': 'Najaf',
        'name': 'نجف 🇮🇶',
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
            'internationalId': 19,
        }
    },
    'اربیل 🇮🇶': {
        'id': 33,
        'title': 'Erbil',
        'name': 'اربیل 🇮🇶',
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
            'internationalId': 20,
        }
    },
    'بغداد 🇮🇶': {
        'id': 54,
        'title': 'Baghdad',
        'name': 'بغداد 🇮🇶',
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
            'internationalId': 21,
        }
    },
    'سلیمانیه 🇮🇶': {
        'id': 36,
        'title': 'Sulaymaniyah',
        'name': 'سلیمانیه 🇮🇶',
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
            'internationalId': 22,
        }
    },
    'مسقط 🇴🇲': {
        'id': 7,
        'title': 'Muscat',
        'name': 'مسقط 🇴🇲',
        'airport': 'فرودگاه بین‌المللی مسقط',
        'airportCode': 'MCT',
        'timezone': 'Asia/Muscat',
        'timezoneOffsetStr': '+04:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 23,
        }
    },
    'مسکو (شرمتیوو) 🇷🇺': {
        'id': 23,
        'title': 'Moscow_Sheremetyevo',
        'name': 'مسکو (شرمتیوو) 🇷🇺',
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
            'internationalId': 24,
        }
    },
    'مسکو (ونوکووا) 🇷🇺': {
        'id': 40,
        'title': 'Moscow Vnukovo',
        'name': 'مسکو (ونوکووا) 🇷🇺',
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
            'internationalId': 25,
        }
    },
    'ایروان 🇦🇲': {
        'id': 11,
        'title': 'Yerevan',
        'name': 'ایروان 🇦🇲',
        'airport': 'Zvartnots International Airport',
        'airportCode': 'EVN',
        'timezone': 'Asia/Yerevan',
        'timezoneOffsetStr': '+04:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 26,
        }
    },
    'دهلی 🇮🇳' : {
        'id': 42,
        'title': 'DELHI',
        'name': 'دهلی 🇮🇳',
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
            'internationalId': 27,
        }
    },
    'بمبئی 🇮🇳': {
        'id': 52,
        'title': 'Mumbai',
        'name': 'بمبئی 🇮🇳',
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
            'internationalId': 28,
        }
    },
    'بانکوک 🇹🇭' : {
        'id': 46,
        'title': 'Bangkok',
        'name': 'بانکوک 🇹🇭',
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
            'internationalId': 29,
        }
    },
    'وارنا 🇧🇬' : {
        'id': 49,
        'title': 'Varna',
        'name': 'وارنا 🇧🇬',
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
            'internationalId': 30,
        }
    },
    'لاهور 🇵🇰' : {
        'id': 51,
        'title': 'Lahore',
        'name': 'لاهور 🇵🇰',
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
            'internationalId': 31,
        }
    },
    'کراچی 🇵🇰': {
        'id': 64,
        'title': 'Karachi',
        'name': 'کراچی 🇵🇰',
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
            'internationalId': 32,
        }
    },
    'بیروت 🇱🇧' : {
        'id': 57,
        'title': 'Beirut',
        'name': 'بیروت 🇱🇧',
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
            'internationalId': 33,
        }
    },
    'فرانکفورت 🇩🇪' : {
        'id': 60,
        'title': 'Frankfurt',
        'name': 'فرانکفورت 🇩🇪',
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
            'internationalId': 34,
        }
    },
    'هامبورگ 🇩🇪' : {
        'id': 66,
        'title': 'Hamburg',
        'name': 'هامبورگ 🇩🇪',
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
            'internationalId': 35,
        }
    },
    'تاشکند 🇺🇿' : {
        'id': 67,
        'title': 'Tashkent',
        'name': 'تاشکند 🇺🇿',
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
            'internationalId': 36,
        }
    },
    'دوشنبه 🇹🇯' : {
        'id': 70,
        'title': 'Dushanbe',
        'name': 'دوشنبه 🇹🇯',
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
            'internationalId': 37,
        }
    },
    'پاریس 🇫🇷' : {
        'id': 73,
        'title': 'Paris',
        'name': 'پاریس 🇫🇷',
        'airport': {
            'en': 'Paris Airport',
            'fa': 'فرودگاه پاریس',
        },
        'airportCode': 'PAR',
        'timezone': 'Europe/Paris',
        'timezoneOffsetStr': '+02:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 38,
        }
    },
    'وین 🇦🇹' : {
        'id': 77,
        'title': 'Vienna',
        'name': 'وین 🇦🇹',
        'airport': {
            'en': 'Vienna Airport',
            'fa': 'فرودگاه وین',
        },
        'airportCode': 'VIE',
        'timezone': 'Europe/Vienna',
        'timezoneOffsetStr': '+02:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 39,
        }
    },
    'ریمینی 🇮🇹': {
        'id': 29,
        'title': 'Rimini_Italy',
        'name': 'ریمینی 🇮🇹',
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
            'internationalId': 40,
        }
    },
    'گوانگچو 🇰🇷' : {
        'id': 78,
        'title': 'Guangzhou',
        'name': 'گوانگچو 🇰🇷',
        'airport': {
            'en': 'Guangzhou Airport',
            'fa': 'فرودگاه گوانگچو',
        },
        'airportCode': 'KWJ',
        'timezone': 'Asia/Shanghai',
        'timezoneOffsetStr': '+08:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 41,
        }
    },
    'باکو 🇦🇿' : {
        'id': 81,
        'title': 'Baku',
        'name': 'باکو 🇦🇿',
        'airport': {
            'en': 'Baku Airport',
            'fa': 'فرودگاه باکو',
        },
        'airportCode': 'GYD',
        'timezone': 'Asia/Baku',
        'timezoneOffsetStr': '+04:00',
        'type': {
            'domestic': False,
            'domesticId': False,
            'international': True,
            'internationalId': 42,
        }
    },
    'آلماتی 🇰🇿': {
        'id': 39,
        'title': 'Almaty',
        'name': 'آلماتی 🇰🇿',
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
            'internationalId': 43,
        }
    },
}

# Flight commission rates
flights_commission = {
    'اکونومی': 0.05,
    'سیستمی': 0.07,
    'بیزینس': 0.09,
}

# Channel IDs
channels_ids = {
    "Parvaz_charters": -1001882499515,
}