import unittest
import datetime
from userstories_sp import *

class TestProject(unittest.TestCase):
    """
    List all people in a GEDCOM file who were born in the last 30 days
    """
    def test_us35_ppl_born_last_30days_check(self):
        # Assure that the dates are in properformat
        # template : us35_ppl_born_last_30days_check(birth_date,present_date)
       
        # if the birth date is NA it must be false
        self.assertFalse(userstories_sp.us35_ppl_born_last_30days_check("NA"))

        # If birth date is after present date
        self.assertFalse(userstories_sp.us35_ppl_born_last_30days_check("2020-02-22"))

         # if birth date is before more than 30 days in the past from current date
        self.assertFalse(userstories_sp.us35_ppl_born_last_30days_check("2018-04-13"))

        # If the birth date is within 30 days from current date, it should be true
        self.assertTrue(userstories_sp.us35_ppl_born_last_30days_check("2019-03-22"))

       

       
        


if __name__ == '__main__':
    unittest.main()
