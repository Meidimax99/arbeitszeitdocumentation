import calendar
import datetime
cal = calendar.Calendar()

string = "2020-1"

year = int(string.split('-')[0])
month = int(string.split('-')[1])

def last_day_of_month(any_day):
    # this will never fail https://stackoverflow.com/questions/42950/how-to-get-the-last-day-of-the-month?page=1&tab=votes#tab-top
    # get close to the end of the month for any day, and add 4 days 'over'
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
    return next_month - datetime.timedelta(days=next_month.day)
#


#dte from string
#first day
dt= datetime.datetime.strptime(string, "%Y-%m").date()
print(dt.day)

lastDay = last_day_of_month(dt)
print(lastDay)