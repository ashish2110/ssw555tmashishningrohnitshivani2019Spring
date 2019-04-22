import unittest
import datetime
from userstories_sp import *

class TestProject(unittest.TestCase):
    """
    Parents should not marry any of their children
    """
    def test_us17_parent_ntmarry_children_check(self):
        # Assure that the dates are in properformat
        # template : us17_parent_ntmarry_children_check(mother_id,father_id,child_id)

        # If birth date is after present date
        self.assertFalse(userstories_sp.us17_parent_ntmarry_children_check("@I1@","@I2@","@I1@"))

         # if birth date is before more than 30 days in the past from current date
        self.assertFalse(userstories_sp.us17_parent_ntmarry_children_check("@I2@","@I1@","@I1@"))

        # If the birth date is within 30 days from current date, it should be true
        self.assertTrue(userstories_sp.us17_parent_ntmarry_children_check("@I1@","@I2@","@I3@"))


if __name__ == '__main__':
    unittest.main()
