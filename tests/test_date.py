import lib.date as date
import lib.leap_year as leap_year
import unittest


class TestDateValidation(unittest.TestCase):
    def test_invalid_before_date(self):
        #start_date = date.Date(1, 1, 2002)
        date.Date(1,1,1600)
        self.assertRaises(ValueError, date.Date, 1, 1, 1600)

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


class TestDateDiff(unittest.TestCase):
    def test_diff_same_month_0(self):
        date1 = date.Date(2, 1, 2000)
        date2 = date.Date(1, 1, 2000)
        self.assertEqual(date1.diff(date2),0)

    # test case given
    def test_diff_same_month_1(self):
        date1 = date.Date(22, 6, 1983)
        date2 = date.Date(2, 6, 1983)
        self.assertEqual(date1.diff(date2), 19)

    # test case given
    def test_diff_same_day(self):
        date1 = date.Date(22, 6, 1983)
        date2 = date.Date(22, 6, 1983)
        self.assertEqual(date1.diff(date2), 0)

    def test_diff_same_month_neg(self):
        date1 = date.Date(2, 6, 1983)
        date2 = date.Date(22, 6, 1983)
        self.assertEqual(date1.diff(date2), -19)

    def test_diff_diff_month(self):
        date1 = date.Date(22, 7, 2022)
        date2 = date.Date(2, 6, 2022)
        self.assertEqual(date1.diff(date2), 49)

    def test_diff_diff_month2(self):
        date1 = date.Date(2, 7, 2022)
        date2 = date.Date(22, 6, 2022)
        self.assertEqual(date1.diff(date2), 9)

    def test_diff_1year(self):
        date1 = date.Date(22, 6, 2023)
        date2 = date.Date(22, 6, 2022)
        self.assertEqual(date1.diff(date2), 364)

    def test_diff_2year(self):
        date1 = date.Date(22, 6, 2023)
        date2 = date.Date(22, 6, 2021)
        self.assertEqual(date1.diff(date2), 729)

    # test example 2
    def test_diff_example2(self):
        date1 = date.Date(25, 12, 1984)
        date2 = date.Date(4, 7, 1984)
        self.assertEqual(date1.diff(date2), 173)

    def test_diff_example3(self):
        date1 = date.Date(3, 1, 1989)
        date2 = date.Date(3, 8, 1983)
        self.assertEqual(date1.diff(date2), 1979)

    def test_diff_example3_neg(self):
        date1 = date.Date(3, 8, 1983)
        date2 = date.Date(3, 1, 1989)
        self.assertEqual(date1.diff(date2), -1979)


class TestMonthDiff(unittest.TestCase):

    def test_diff_diff_month(self):
        date1 = date.Date(2, 7, 2022)
        self.assertEqual(date1.__diff_month__(7,6), 30)

    def test_diff_diff_month2(self):
        date1 = date.Date(2, 8, 2022)
        self.assertEqual(date1.__diff_month__(8,6), 61)

    def test_diff_diff_month2_neg(self):
        date1 = date.Date(2, 6, 2022)
        self.assertEqual(-61, date1.__diff_month__(6,8))


class TestLessThanOrEqual(unittest.TestCase):

    def test_less_than_year(self):
        date1 = date.Date(22, 6, 2023)
        date2 = date.Date(22, 6, 2021)
        self.assertFalse(date1.less_than_or_equal(date2))

    def test_less_than_month(self):
        date1 = date.Date(22, 6, 2023)
        date2 = date.Date(22, 5, 2023)
        self.assertFalse(date1.less_than_or_equal(date2))

    def test_less_than_day(self):
        date1 = date.Date(22, 6, 2023)
        date2 = date.Date(21, 6, 2023)
        self.assertFalse(date1.less_than_or_equal(date2))

    def test_less_than_year_neg(self):
        date1 = date.Date(22, 6, 2023)
        date2 = date.Date(22, 6, 2025)
        self.assertTrue(date1.less_than_or_equal(date2))

    def test_less_than_month_neg(self):
        date1 = date.Date(22, 6, 2023)
        date2 = date.Date(22, 7, 2023)
        self.assertTrue(date1.less_than_or_equal(date2))

    def test_less_than_day_neg(self):
        date1 = date.Date(22, 6, 2023)
        date2 = date.Date(23, 6, 2023)
        self.assertTrue(date1.less_than_or_equal(date2))

    def test_less_than_equal(self):
        date1 = date.Date(22, 6, 2023)
        date2 = date.Date(22, 6, 2023)
        self.assertTrue(date1.less_than_or_equal(date2))


if __name__ == "__main__":
    unittest.main()
