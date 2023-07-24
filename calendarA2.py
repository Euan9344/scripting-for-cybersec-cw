import calendar
import datetime

def current_month():

    now = datetime.datetime.now()

    # Print the calendar for the current month
    print(calendar.month(now.year, now.month))

current_month()