import unittest
from us_rs import us_rs

class TestSiblingCount(unittest.TestCase):
    

    # User Story 7
    def test_siblingCount(self):
        
        
        
        family_right_1 = {'@F1@': {'HUSB': '@I2@', 'WIFE': '@I3@', 'CHIL': ['@I1@', '@I4@'], 'MARR_DATE': '1994-06-12', 'DIV_DATE': 'NA'}, '@F2@': {'HUSB': '@I7@', 'WIFE': '@I8@', 'CHIL': ['@I2@'], 'MARR_DATE': '1970-02-03', 'DIV_DATE': 'NA'}, '@F3@': {'HUSB': '@I5@', 'WIFE': '@I6@', 'CHIL': ['@I3@'], 'MARR_DATE': '1992-03-10', 'DIV_DATE': 'NA'}, '@F4@': {'HUSB': '@I9@', 'WIFE': '@I11@', 'CHIL': ['@I14@'], 'MARR_DATE': '1998-03-10', 'DIV_DATE': 'NA'}, '@F5@': {'HUSB': '@I7@', 'WIFE': '@I10@', 'CHIL': ['@I9@'], 'MARR_DATE': '1974-02-05', 'DIV_DATE': 'NA'}, '@F6@': {'HUSB': '@I12@', 'WIFE': '@I13@', 'CHIL': ['@I11@'], 'MARR_DATE': '1977-12-06', 'DIV_DATE': 'NA'}}
        

        #Object with empty "CHIL"
        family_right_2 = {"@F1": {"CHIL": []}}
        
        #Object with no "CHIL" key
        family_right_3 = {"@F1": {}}
        
        #Family of 15 children thus all children have 14 siblings. Thus it should work
        family_right_4 = {'@F1@': {'CHIL': ["@I1@", "@I2@","@I3@","@I4@","@I5@","@I6@","@I7@","@I8@","@I9@","@I10@","@I11@","@I12@","@I13@","@I14@","@I15@" ]}}

        #Family of 16 Children thus all children have 15 siblings, thus case fails
        # For the sake of simplicity I have added a line number to the first element, since our code would detect the first line 
        # because of which error rises.
        family_wrong = {'@F1@': {'CHIL': [["@I1@", 10], "@I2@","@I3@","@I4@","@I5@","@I6@","@I7@","@I8@","@I9@","@I10@","@I11@","@I12@","@I13@","@I14@","@I15@","@I16@" ]}}
        
        #Passing random string instead of a dictionary
        

        self.assertTrue(us_rs.siblingCount(family_right_1))
        self.assertTrue(us_rs.siblingCount(family_right_2))
        self.assertTrue(us_rs.siblingCount(family_right_3))
        self.assertTrue(us_rs.siblingCount(family_right_4))
        self.assertFalse(us_rs.siblingCount(family_wrong))
        
        
        



if __name__ == "__main__":
    unittest.main()

