# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
#
# days_in_month(year=2022, month=2)
# And it will use this information to work out the number of days in the month, then return that as the output, e.g.:
#
# 28
# The List month_days contains the number of days in a month from January to December
# for a non-leap year. A leap year has 29 days in February.
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def days_in_month(year, month):
    if month <= 12:
        if is_leap_year(year) and month == 2:
            return 29
        return month_days[month - 1]
    else:
        return "months can not be greater than 12"


year = int(input("Enter a year: "))
month = int(input("enter a month (by number): "))
days = days_in_month(year, month)
print(f"{days}")
