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
       
        # if the child/mother/father birth date is NA it must be false
        self.assertFalse(userstories_sp.us12_parent_child_agediff_limit_check("NA","1970-04-12","1950-05-06"))
        self.assertFalse(userstories_sp.us12_parent_child_agediff_limit_check("2012-02-23","NA","1950-05-06"))
        self.assertFalse(userstories_sp.us12_parent_child_agediff_limit_check("2012-02-23","1970-04-12","NA"))

        # If mother is more than 60 year older than the child
        self.assertFalse(userstories_sp.us12_parent_child_agediff_limit_check("2012-02-23","1940-04-12","1950-05-06"))

         #  If mother is more than 80 year older than the child
        self.assertFalse(userstories_sp.us12_parent_child_agediff_limit_check("2012-02-23","1970-04-12","1920-05-06"))

        # If mother is less than 60 year older and father is less than 80 year older than the child
        self.assertTrue(userstories_sp.us12_parent_child_agediff_limit_check("2012-02-23","1970-04-12","1950-05-06"))

       

if __name__ == '__main__':
    unittest.main()
