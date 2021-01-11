import date

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


def number_of_leap_days(start_date,end_date):
    """
    Returns the number of leap days between the two dates
    :param start_date:
    :param end_date:
    :return:
    """
    #date(1,2,200)
    #if start_date
    return 0
