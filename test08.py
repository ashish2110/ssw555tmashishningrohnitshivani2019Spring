import unittest
import datetime
# from dateutil import relativedelta
from userstories_sp import *

class TestProject(unittest.TestCase):
    """
    List all people in a GEDCOM file who were born in the last 30 days
    """
    def test_us08_child_born_after_parents_marriagedate(self):
        # Assure that the dates are in properformat
        # template : us08_child_parents_marriagedate_check(marriage_date,child_birth_date,divorce_date)

        # if divorce date is NA and child birth date is greater than parent marriage date
        self.assertTrue(userstories_sp.us08_child_parents_marriagedate_check("1985-03-02","1986-03-02","NA"))

        # if divorce date is NA and child birth date is smaller than parent marriage date
        self.assertFalse(userstories_sp.us08_child_parents_marriagedate_check("1987-03-02","1985-03-02","NA"))

        # if Child is born 9 months after parent's divorce
        self.assertFalse(userstories_sp.us08_child_parents_marriagedate_check("1987-03-02","1989-03-02",["1988-03-02",12]))

        #If Child is born 9 months within parent's divorce
        self.assertTrue(userstories_sp.us08_child_parents_marriagedate_check("1987-03-02","1990-05-05",["1990-03-02",56]))


      
if __name__ == '__main__':
    unittest.main()