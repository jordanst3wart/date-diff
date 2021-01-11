import months
import leap_year


def __validate_date__(day, month, year):
    if 1901 > year > 3000:
        raise InvalidDate("Invalid year")

    if 0 > month > 12:
        raise InvalidDate("Invalid month")

    if 0 > day:
        pass

    if day > 31:
        raise InvalidDate("Invalid day")
    elif day == 31 and months.short_months.contains(month):
        raise InvalidDate("Invalid day")
    elif day > 28 and month == 2:
        raise InvalidDate("Invalid day in Feburary")
    elif day == 28 and month == 2 and not leap_year.is_leap_year(year):
        raise InvalidDate("Invalid day not leap year")


class Date:
    """
    Dates between, and not including 1900 and 3000
    """
    def __init__(self, day, month, year):
        __validate_date__(day, month, year)
        self.day = day
        self.month = month
        self.year = year

    def diff(self, date):
        pass

# 1901-01-01 and 2999-12-31

class InvalidDate(Exception):
    """Invalid date."""
    # TODO should print error message
    def __init__(self, message):
        self.message = message
