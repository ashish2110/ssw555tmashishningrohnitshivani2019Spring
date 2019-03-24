import unittest
from us_ny import us10_tsk01_is_child_marriage

class TestProject(unittest.TestCase):
    def test_us10_tsk01_is_child_marriage(self):
        # sequence: date of marriage, husband date of birth, wife date of birth
        # Non-parseable input are considered as false
        self.assertFalse(us10_tsk01_is_child_marriage("NA", "NA", "NA"))
        self.assertFalse(us10_tsk01_is_child_marriage("Invalid", "Invalid", "Invalid"))
        self.assertFalse(us10_tsk01_is_child_marriage("Random", "Nonsense", "Whatever"))
        self.assertFalse(us10_tsk01_is_child_marriage("1922-02-30", "1988-03", "2022-04-13"))
        # Parents old enough
        self.assertFalse(us10_tsk01_is_child_marriage("1989-12-18", "1961-12-08", "1966-03-11"))
        # Parent(s) too young
        self.assertTrue(us10_tsk01_is_child_marriage("2018-05-05", "2005-04-13", "2006-02-13"))
        self.assertTrue(us10_tsk01_is_child_marriage("2008-06-07", "1990-07-30", "1996-11-11"))
        self.assertTrue(us10_tsk01_is_child_marriage("2008-06-07", "1996-11-11", "1990-07-30"))

if __name__ == '__main__':
    unittest.main()