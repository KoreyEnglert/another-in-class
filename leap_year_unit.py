import unittest
import leap_year_modified

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(leap_year_modified.is_leap_year(2000), True);

    def test_add2(self):
        self.assertEqual(leap_year_modified.is_leap_year(2001), False);

    def test_add3(self):
        self.assertEqual(leap_year_modified.is_leap_year(1900), False);

    def test_add4(self):
        self.assertEqual(leap_year_modified.is_leap_year(2000), False);

    def test_add5(self):
        self.assertEqual(leap_year_modified.is_leap_year(-400), True);

    def test_add6(self):
        self.assertEqual(leap_year_modified.is_leap_year("a"), False);

if __name__ == '__main__':
    unittest.main()
