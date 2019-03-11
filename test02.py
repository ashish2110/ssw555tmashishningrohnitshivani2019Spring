import unittest
from userstories_sp import *


class TestProject(unittest.TestCase):
    
    """
    Birth should occur before marriage of an individual
    """

    incorrect_ind = {
        '@I1@': {'NAME': ['Adam /Levine/', 17], 'SEX': ['M', 21], 'BIRT_DATE': ['1964-02-25', 23], 'DEAT_DATE': ['2001-01-31', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'False', 'FAMS': [['@F1@', 26]]},
        '@I2@': {'NAME': ['Sherley /Johnson/', 17], 'SEX': ['F', 21], 'BIRT_DATE': ['2000-02-25', 23], 'DEAT_DATE': ['NA', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'True', 'FAMS': [['@F1@', 26]]}
        }

    incorrect_family = {'@F1@': {'HUSB': ['@I1@', 139], 'WIFE': ['@I2@', 140], 'CHIL': [['NA']], 'MARR_DATE': ['1995-03-02', 143], 'DIV_DATE': ['1972-03-28', 153]}
    }
    def test_us02_birth_is_before_marriage(self):
        # Assure that the dates are in properformat
        # template :  us02_birth_is_before_marriage(birth_date,marriage_date)

        # if any of the two dates are "NA"
        self.assertTrue(userstories_sp.us02_birth_is_before_marriage("NA","1985-03-02"))
        self.assertTrue(userstories_sp.us02_birth_is_before_marriage("1985-03-02","NA"))

        # if both the dates are "NA"
        self.assertTrue(userstories_sp.us02_birth_is_before_marriage("NA","NA"))

        # if birth date  is before the marriage date, it is true
        self.assertTrue(userstories_sp.us02_birth_is_before_marriage("1978-11-24","1990-12-18"))

        # if birth date  is after the marriage date, it is false
        self.assertFalse(userstories_sp.us02_birth_is_before_marriage("2019-04-13","2000-06-15"))
        
        
        #if there is an error in the user story, it will print the error and return false
        self.assertFalse(userstories_sp.us02_birth_before_marriage(self.incorrect_ind,self.incorrect_family))


if __name__ == '__main__':
    unittest.main()
