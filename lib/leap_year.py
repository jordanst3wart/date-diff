import lib.date as date


def is_leap_year(year: int):
    """
    Returns true if a leap year
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
    Returns the number of leap days between the two dates
    :param start_date:
    :param end_date:
    :return:
    """



    if date1.year == date2.year and is_leap_year(date1.year):
        return 0

    # check if part years include feburary and are a leap year
    # if year1 == year2 and year1 == leap_year
    # check if months include feburary
    # check if days include feburary

    # iterate over years
    range(date1.year, date2.year)

    #date(1,2,200)
    #if start_date
    return 0


def is_leap_day(date):
    pass

