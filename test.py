result = {
  1: {
    'Price': '7,406,100',
    'freeSeats': '5',
    'departure': '20:00',
    'company': 'هواپیمایی معراج',
    'flightNumber': '4805'
  },
  2: {
    'Price': '7,406,100',
    'freeSeats': '5',
    'departure': '22:00',
    'company': 'هواپیمایی آتا',
    'flightNumber': '6609'
  },
  3: {
    'Price': '7,406,100',
    'freeSeats': '3',
    'departure': '08:00',
    'company': 'هواپیمایی آتا',
    'flightNumber': '6619'
  }
}

# get the first key of result dictionary
print(list(result.keys())[0])
print(list(result.keys())[-1])
#
# i = 1
# while i <16:
#   print(result[i]['Price'])
#   i+=1

# #
# #
# # print(result[1]['Price'])
#
# dates = {
#     1: '1401-06-20',
#     2: '1401-06-21',
# }
# i = 1
# while i < 3:
#     print(dates[i])
#     i +=1
# import timeIR
#
# print(int(timeIR.ShowTodayFull()[:4]))
# print(int(timeIR.ShowTodayFull()[6:7]))
# print(int(timeIR.ShowTodayFull()[8:11]))

# from persiantools.jdatetime import JalaliDate
# import datetime
# print(JalaliDate.today())
# a = []
# i = 0
# while i < 31:
#     duration = JalaliDate(JalaliDate.today()) + datetime.timedelta(days=i)
#     a.append(duration.isoformat())
#     print(duration)
#     i+=1
#
# print(a)


# a = ['سلام', 'خوبی']
#
# text = ''
# for i in a:
#     text += i
#

# print(text)

# from persiantools.jdatetime import JalaliDate, JalaliDateTime
# import datetime
#
# def jalaiDates(today):
#     dates = {}
#     i = 1
#     while i < 30:
#       dates[i] = (JalaliDate(today) + datetime.timedelta(days=i)).isoformat()
#       i += 1
#     print(dates)


# jalaiDates(JalaliDate.today())


