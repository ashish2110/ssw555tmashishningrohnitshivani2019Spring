import unittest
import datetime
from userstories_sp import *

class TestProject(unittest.TestCase):
    """
    List all people in a GEDCOM file who were born in the last 30 days
    """
    def test_us09_child_birth_parent_death_check(self):
        # Assure that the dates are in properformat
        # template : us09_child_birth_parent_death_check(mother_death_date,father_death_date,child_birth_date)

        # if child is born before death of mother and father is alive(ie death date NA) 
        self.assertTrue(userstories_sp.us09_child_birth_parent_death_check(["1985-03-02",23],"NA",["1984-03-02",89]))

        # if child is born after death of mother and father is alive(ie death date NA) 
        self.assertFalse(userstories_sp.us09_child_birth_parent_death_check(["1987-03-02",12],"NA",["1990-03-02",45]))

        # if child is born before 9 months after death of father and mother is alive(ie death date NA) 
        self.assertTrue(userstories_sp.us09_child_birth_parent_death_check("NA",["1989-03-02",45],["1988-11-02",12]))

        # if child is born after 9 months after death of father and mother is alive(ie death date NA) 
        self.assertFalse(userstories_sp.us09_child_birth_parent_death_check("NA",["1990-05-05",9],["2001-03-02",56]))

        # if child is born before death of mother and before 9 months after death of father
        self.assertTrue(userstories_sp.us09_child_birth_parent_death_check(["1989-10-02",62],["1989-01-02",45],["1988-11-02",12]))

        # if child is born before death of mother and after 9 months after death of father
        self.assertFalse(userstories_sp.us09_child_birth_parent_death_check(["1989-10-02",62],["1987-01-02",45],["1988-11-02",12]))

        # if child is born after death of mother and before 9 months after death of father
        self.assertFalse(userstories_sp.us09_child_birth_parent_death_check(["1987-10-02",62],["1988-09-02",45],["1988-11-02",12]))

        # if child is born after death of mother and after 9 months after death of father
        self.assertFalse(userstories_sp.us09_child_birth_parent_death_check(["1987-10-02",62],["1986-01-02",45],["1988-11-02",12]))



      
if __name__ == '__main__':
    unittest.main()