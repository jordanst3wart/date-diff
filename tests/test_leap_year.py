import lib.leap_year as leap_year
import lib.date as date
import unittest


class TestIsLeapYear(unittest.TestCase):
    def test_is_not_leap_year(self):
        self.assertFalse(leap_year.is_leap_year(2001))

    def test_is_leap_year(self):
        self.assertTrue(leap_year.is_leap_year(2004))

    def test_is_leap_year_hundred(self):
        self.assertFalse(leap_year.is_leap_year(1900))

    def test_is_leap_year_four_hundred(self):
        self.assertTrue(leap_year.is_leap_year(2000))


class TestLeapYearDays(unittest.TestCase):
    def test_leap_days_zero(self):
        start_date = date.Date(1, 1, 2002)
        end_date = date.Date(2, 1, 2002)
        diff = leap_year.number_of_leap_days(start_date, end_date)
        self.assertEqual(diff, 0)

    def test_leap_days_leap_year(self):
        start_date = date.Date(1, 1, 2004)
        end_date = date.Date(1, 1, 2005)
        diff = leap_year.number_of_leap_days(start_date, end_date)
        self.assertEqual(diff, 1)


if __name__ == "__main__":
    unittest.main()
