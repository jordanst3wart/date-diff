import lib.date as date


def is_leap_year(year: int):
    """
    :year year: the year
    :return: true if a leap year
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def number_of_leap_days(date1, date2):
    """
    :param date1: a date value
    :param date2: a date value
    :return: the number of leap days between two dates
    """
    days = 0
    # negative case
    if date1.less_than_or_equal(date2):
        return number_of_leap_days(date2, date1) * -1

    days += full_leap_years(date1.year, date2.year)

    if start_before_leap_day(date2):
        days += 1
    if end_after_leap_day(date1):
        days += 1
    if date1.year == date2.year and end_after_leap_day(date1) and start_before_leap_day(date2):
        days -= 1
    return days


# check for complete years
def full_leap_years(year1, year2):
    days = 0
    if year1 - 3 > year2:
        full_year1 = year1
        full_year2 = year2 + 1
        for i in range(full_year2, full_year1):
            if is_leap_year(i):
                days += 1
    return days


def start_before_leap_day(date1):
    if is_leap_year(date1.year):
        if date1.month < 2:
            return True
        elif date1.month == 2 and date1.day < 29:
            return True
        else:
            return False


def end_after_leap_day(date1):
    if is_leap_year(date1.year):
        if date1.month > 2:
            return True
        else:
            return False

