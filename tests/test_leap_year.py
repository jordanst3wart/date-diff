from lib.leap_year import is_leap_year, number_of_leap_days
from lib.date import Date
import unittest


class TestIsLeapYear(unittest.TestCase):
    def test_is_not_leap_year(self):
        self.assertFalse(is_leap_year(2001))

    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2004))

    def test_is_leap_year_hundred(self):
        self.assertFalse(is_leap_year(1900))

    def test_is_leap_year_four_hundred(self):
        self.assertTrue(is_leap_year(2000))


class TestLeapYearDays(unittest.TestCase):
    def test_leap_days_zero_day(self):
        start_date = Date(1, 1, 2002)
        end_date = Date(2, 1, 2002)
        diff = number_of_leap_days(start_date, end_date)
        self.assertEqual(diff, 0)

    def test_leap_days_zero_month(self):
        start_date = Date(1, 1, 2002)
        end_date = Date(1, 2, 2002)
        diff = number_of_leap_days(start_date, end_date)
        self.assertEqual(diff, 0)

    def test_leap_days_zero_year(self):
        start_date = Date(1, 1, 2002)
        end_date = Date(1, 1, 2003)
        diff = number_of_leap_days(start_date, end_date)
        self.assertEqual(diff, 0)

    def test_leap_days_leap_day(self):
        date1 = Date(1, 3, 2004)
        date2 = Date(28, 2, 2004)
        diff = number_of_leap_days(date1, date2)
        self.assertEqual(diff, 1)

    def test_leap_days_leap_month(self):
        date1 = Date(28, 3, 2004)
        date2 = Date(28, 1, 2004)
        diff = number_of_leap_days(date1, date2)
        self.assertEqual(diff, 1)

    def test_leap_days_leap_year(self):
        date1 = Date(1, 1, 2005)
        date2 = Date(1, 1, 2004)
        diff = number_of_leap_days(date1, date2)
        self.assertEqual(diff, 1)

    def test_leap_days_leap_between_years(self):
        date1 = Date(1, 1, 2007)
        date2 = Date(1, 1, 2002)
        diff = number_of_leap_days(date1, date2)
        self.assertEqual(diff, 1)

    def test_leap_days_leap_between_years2(self):
        date1 = Date(1, 1, 2007)
        date2 = Date(1, 9, 1999)
        diff = number_of_leap_days(date1, date2)
        self.assertEqual(diff, 2)

    def test_leap_days_leap_starting_after(self):
        date1 = Date(1, 1, 2002)
        date2 = Date(1, 3, 2000)
        diff = number_of_leap_days(date1, date2)
        self.assertEqual(diff, 0)

    def test_leap_days_leap_ending_before(self):
        date1 = Date(28, 2, 2004)
        date2 = Date(1, 11, 2000)
        diff = number_of_leap_days(date1, date2)
        self.assertEqual(diff, 0)

    def test_leap_days_leap_year_counting(self):
        date1 = Date(1, 1, 2021)
        date2 = Date(1, 1, 1966)
        diff = number_of_leap_days(date1, date2)
        self.assertEqual(diff, 14)

    def test_leap_days_leap_year_multiple(self):
        date1 = Date(1, 1, 2009)
        date2 = Date(1, 1, 2004)
        diff = number_of_leap_days(date1, date2)
        self.assertEqual(diff, 2)

    def test_leap_days_leap_year_multiple2(self):
        date1 = Date(1, 1, 2009)
        date2 = Date(1, 1, 2005)
        diff = number_of_leap_days(date1, date2)
        self.assertEqual(diff, 1)

    def test_leap_days_odd_case(self):
        date1 = Date(2, 1, 2000)
        date2 = Date(1, 1, 2000)
        diff = number_of_leap_days(date1, date2)
        self.assertEqual(diff, 0)

    def test_leap_days_odd_case2(self):
        date1 = Date(2, 3, 2000)
        date2 = Date(1, 3, 2000)
        diff = number_of_leap_days(date1, date2)
        self.assertEqual(diff, 0)


if __name__ == "__main__":
    unittest.main()
