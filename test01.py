import unittest
from us_ny import us01_tsk01_is_b4_now

class TestProject(unittest.TestCase):
    #pre-condition: date string format is correct if date is available
    def test_us01_tsk01_is_b4_now(self):
        # if date is not available, it is considered as true
        self.assertTrue(us01_tsk01_is_b4_now("NA"))
        # if date is before current date, it is true
        self.assertTrue(us01_tsk01_is_b4_now("1990-12-18"))
        self.assertTrue(us01_tsk01_is_b4_now("1980-02-13"))
        # if date is after current date, it is false
        self.assertFalse(us01_tsk01_is_b4_now("2019-04-13"))
        self.assertFalse(us01_tsk01_is_b4_now("2022-03-11"))

if __name__ == '__main__':
    unittest.main()