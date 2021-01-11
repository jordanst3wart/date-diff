#import months
#import leap_year
import src.leap_year as leap_year
#import src.months as months


# set of long months
# long_months = {}
# set of short months
short_months = {4, 6, 9, 11}

days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


class Date:
    """
    Dates between, and not including 1900 and 3000
    """
    def __init__(self, day, month, year):
        if 1901 > year > 3000:
            raise ValueError("Invalid year")
        elif 0 > month > 12:
            raise ValueError("Invalid month")
        elif 0 > day > 31:
            raise ValueError("Invalid day")
        elif day == 31 and month in short_months:
            raise ValueError("Invalid day")
        elif day > 29 and month == 2:
            raise ValueError("Invalid day in Feburary")
        elif day == 29 and month == 2 and not leap_year.is_leap_year(year):
            raise ValueError("Invalid day not leap year")
        else:
            self.day = day
            self.month = month
            self.year = year

    def diff(self, date):
        # break down to days
        days = self.day - date.day
        month_to_days = self.__diff_month__(self,date.month)
        year_to_days = (self.year - date.year) * 365
        leap_days = 0
        return days + month_to_days + year_to_days + leap_days

    def __diff_month__(self, month):
        days = 0
        # be negative if counting down
        for i in range(self.month, month):
            days += days_in_month[i]

        if self.month < month:
            days *= -1

        return days



