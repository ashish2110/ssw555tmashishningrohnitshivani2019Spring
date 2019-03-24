import unittest
from us_ny import us42_tsk01_is_legit_date

class TestProject(unittest.TestCase):
    def test_us42_tsk01_is_legit_date(self):
        self.assertFalse(us42_tsk01_is_legit_date("NA"))
        self.assertFalse(us42_tsk01_is_legit_date("30 FEB 2015"))
        self.assertFalse(us42_tsk01_is_legit_date("31 Sep 2010"))
        # Partial dates are considered as illegitimate
        self.assertFalse(us42_tsk01_is_legit_date("Sep 2010"))

        self.assertTrue(us42_tsk01_is_legit_date("04 Apr 1990"))
        self.assertTrue(us42_tsk01_is_legit_date("29 Feb 2004"))

if __name__ == '__main__':
    unittest.main()