import lib.leap_year as leap_year
import lib.months as months



class Date:
    """
    Dates between, and not including 1900 and 3000
    """
    def __init__(self, day, month, year):
        if 1901 > year or year > 3000:
            raise ValueError("Invalid year")
        elif 0 > month or month > 12:
            raise ValueError("Invalid month")
        elif 0 > day or day > 31:
            raise ValueError("Invalid day")
        elif day == 31 and month in months.short_months:
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
        # same day return 0
        if date.year == self.year and date.month == self.month and date.day == self.day:
            return 0
        # break down to days
        days = self.day - date.day
        month_to_days = self.__diff_month__( self.month, date.month)
        year_to_days = (self.year - date.year) * 365
        leap_days = leap_year.number_of_leap_days(self, date)
        diff = days + month_to_days + year_to_days + leap_days
        # take into account neighbouring days have zero diff
        # I assume return a negative diff is fine
        if diff > 0:
            diff -= 1
        elif diff < 0:
            diff += 1
        return diff

    def __diff_month__(self, month1, month2):
        days = 0
        # negative day case
        if month2 > month1:
            days = self.__diff_month__(month2, month1) * -1
        else:
            for i in range(month2, month1):
                days += months.days_in_month[i]

        return days

    def less_than_or_equal(self, date):
        if self.year > date.year:
            return False
        elif self.year < date.year:
            return True

        if self.month > date.month:
            return False
        elif self.month < date.month:
            return True

        if self.day > date.day:
            return False
        elif self.day < date.day:
            return True

        return True




