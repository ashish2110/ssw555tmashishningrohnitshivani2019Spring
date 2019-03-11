from us_rs import us_rs
import unittest



class testcase(unittest.TestCase):

    correctIndi1 = {
    '@I1@': {'NAME': ['Adam /Levine/', 17], 'SEX': ['M', 21], 'BIRT_DATE': ['1964-02-25', 23], 'DEAT_DATE': ['2001-01-31', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'False', 'FAMS': 'NA'},
    '@I2@': {'NAME': ['Sherley /Johnson/', 17], 'SEX': ['F', 21], 'BIRT_DATE': ['1972-02-25', 23], 'DEAT_DATE': ['NA', 25], 'FAMC': [['@F1@', 26]], 'ALIVE': 'True', 'FAMS': 'NA'}
    }

    correctFam1 = {
    '@F1@': {'HUSB': ['@I1@', 139], 'WIFE': ['@I2@', 140], 'CHIL': [['NA']], 'MARR_DATE': ['1995-03-02', 143], 'DIV_DATE': ['1972-03-28', 153]}
    }
    def testUS06(self):
        self.assertTrue(us_rs.divorceBeforeDeath(self.correctIndi1, self.correctFam1))



if __name__ == "__main__":
    unittest.main()