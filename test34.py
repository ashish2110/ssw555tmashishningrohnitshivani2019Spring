import unittest
from us_ny import us34_tsk01_is_big_age_gap

class TestProject(unittest.TestCase):
    def test_us34_tsk01_is_big_age_gap(self):
        # sequence: date of marriage, husband date of birth, wife date of birth
        # Non-parseable input are considered as false
        self.assertFalse(us34_tsk01_is_big_age_gap("NA", "NA", "NA"))
        self.assertFalse(us34_tsk01_is_big_age_gap("Invalid", "Invalid", "Invalid"))
        self.assertFalse(us34_tsk01_is_big_age_gap("Random", "Nonsense", "Whatever"))
        self.assertFalse(us34_tsk01_is_big_age_gap("1922-02-30", "1988-03", "2022-04-13"))
        # Spouse age gap not too big
        self.assertFalse(us34_tsk01_is_big_age_gap("1989-12-18", "1961-12-08", "1966-03-11"))
        # Spouse age gap too big
        self.assertTrue(us34_tsk01_is_big_age_gap("2018-05-05", "2002-04-13", "1984-02-13"))
        self.assertTrue(us34_tsk01_is_big_age_gap("2018-05-05", "1984-02-13", "2002-04-13"))


if __name__ == '__main__':
    unittest.main()