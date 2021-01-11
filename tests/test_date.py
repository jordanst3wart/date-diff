import src.date as date
import unittest


class TestDate(unittest.TestCase):
    def test_invalid_before_date(self):
        #start_date = date.Date(1, 1, 2002)
        self.assertRaises(date.InvalidDate, date.Date, 1, 1, 1600)

    def test_invalid_after_date(self):
        start_date = date.Date(1, 1, 2004)
        end_date = date.Date(1, 1, 2005)
        diff = leap_year.number_of_leap_days(start_date, end_date)
        self.assertEqual(diff, 1)

    def test_invalid_day(self):
        start_date = date.Date(1, 1, 2004)
        end_date = date.Date(1, 1, 2005)
        diff = leap_year.number_of_leap_days(start_date, end_date)
        self.assertEqual(diff, 1)

    def test_invalid_month(self):
        start_date = date.Date(1, 1, 2004)
        end_date = date.Date(1, 1, 2005)
        diff = leap_year.number_of_leap_days(start_date, end_date)
        self.assertEqual(diff, 1)

    def test_invalid_day_month_combo(self):
        start_date = date.Date(1, 1, 2004)
        end_date = date.Date(1, 1, 2005)
        diff = leap_year.number_of_leap_days(start_date, end_date)
        self.assertEqual(diff, 1)

    def test_leap_day_true(self):
        pass

    def test_leap_day_false(self):
        pass

if __name__ == "__main__":
    unittest.main()
