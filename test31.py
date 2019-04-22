from us_rs import us_rs
import unittest



class testcase(unittest.TestCase):

    correctIndi1 = {
    '@I1@': {'NAME': ['Adam /Levine/', 17], 'SEX': ['M', 21], 'BIRT_DATE': ['1964-02-25', 23], 'DEAT_DATE': ['2001-01-31', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'False', 'FAMS': 'NA', "AGE": 38},
    '@I2@': {'NAME': ['Sherley /Johnson/', 17], 'SEX': ['F', 21], 'BIRT_DATE': ['1972-02-25', 23], 'DEAT_DATE': ['NA', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'True', 'FAMS': 'NA', "AGE": 31},
    "@I3@": {"FAMS": "NA" ,"AGE": 32, "ALIVE": "True"},
    "@I4@": {"FAMS":"NA" , "AGE": 33, "ALIVE": "False"},
    "@I5@": {"FAMS": "NA", "AGE": 23, "ALIVE": "True"}
    }
    incorrectIndi = {
    '@I1@': {'NAME': ['Adam /Levine/', 17], 'SEX': ['M', 21], 'BIRT_DATE': ['1964-02-25', 23], 'DEAT_DATE': ['2001-01-31', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'False', 'FAMS': 'NA', "AGE": 38},
    '@I2@': {'NAME': ['Sherley /Johnson/', 17], 'SEX': ['F', 21], 'BIRT_DATE': ['1972-02-25', 23], 'DEAT_DATE': ['NA', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'True', 'FAMS': ["@I1@"], "AGE": 31},
    "@I3@": {"FAMS": "NA" ,"AGE": 22, "ALIVE": "True"},
    "@I4@": {"FAMS":"NA" , "AGE": 33, "ALIVE": "False"},
    "@I5@": {"FAMS": "NA", "AGE": 23, "ALIVE": "True"}
    }
    
    def testUS31(self):
        
        self.assertTrue(us_rs.listSinglePeopleOver30(self.correctIndi1))
        self.assertFalse(us_rs.listSinglePeopleOver30(self.incorrectIndi))



if __name__ == "__main__":
    unittest.main()