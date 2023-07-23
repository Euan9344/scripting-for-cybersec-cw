import calendar
import datetime

def current_month():
    now = datetime.datetime.now()
    year = now.year
    month = now.month

    # Get the calendar for the current month
    cal = calendar.monthcalendar(year, month)

    # Print the calendar header
    print(calendar.month_name[month], year)
    print("Mon  Tue  Wed  Thu  Fri  Sat  Sun")

    # Print each week's row
    for week in cal:
        row = ""
        for day in week:
            if day == 0:
                row += "     "
            else:
                row += "{:2d}   ".format(day)
        print(row)

# Call the function to print the current month's calendar
current_month()