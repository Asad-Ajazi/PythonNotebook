# summary of 01-07 to find out if it is a leap year/days in a month.
print('Leap year challenge\n')

# Number of days per month list. First 0 placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    """Returns True for leap years and False for non-leap years"""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Returns the number of days in a month in a given year"""

    if not 1 <= month <= 12:
        return 'Invalid month'

    if month == 2 and is_leap_year(year):
        return 29

    return month_days[month]


# uses a function within another function for the if condition
# to determine how many days are in the month for that specific year
print('Is 2019 a leap year?:', is_leap_year(2019))
print('Days in feb 2019:', days_in_month(2019, 2))
print()
print('Is 2020 a leap year?:', is_leap_year(2020))
print('Days in feb 2020:', days_in_month(2020, 2))