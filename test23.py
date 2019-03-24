from us_rs import us_rs
import unittest



class testcase(unittest.TestCase):

    incorrect = {
    '@I1@': {'NAME': ['Adam /Levine/', 17], 'SEX': ['M', 21], 'BIRT_DATE': ['1964-02-25', 23], 'DEAT_DATE': ['2001-01-31', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'False', 'FAMS': 'NA'},
    '@I2@': {'NAME': ['Adam /Levine/', 27], 'SEX': ['F', 21], 'BIRT_DATE': ['1964-02-25', 23], 'DEAT_DATE': ['NA', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'True', 'FAMS': 'NA'}
    }
    correct = {
    '@I1@': {'NAME': ['Adam /Levine/', 17], 'SEX': ['M', 21], 'BIRT_DATE': ['1964-02-25', 23], 'DEAT_DATE': ['2001-01-31', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'False', 'FAMS': 'NA'},
    '@I2@': {'NAME': ['Suzie /Levine/', 27], 'SEX': ['F', 21], 'BIRT_DATE': ['1974-01-5', 23], 'DEAT_DATE': ['NA', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'True', 'FAMS': 'NA'}
    }

   
    def testUS23(self):
        self.assertFalse(us_rs.uniqueNameAndBirthdayCheck(self.incorrect))
        self.assertTrue(us_rs.uniqueNameAndBirthdayCheck(self.correct))




if __name__ == "__main__":
    unittest.main()