import src.date as date
import unittest


class TestDate(unittest.TestCase):
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
