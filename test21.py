import unittest
from userstories_an import *

class testcase(unittest.TestCase):

    def test_21(self):
        result=userstory_an.us_21([['F',4],['M',6],'F1','I1','I2'])
        self.assertEqual(result,["Error US21 in line 4:Gender of husband with I1 id is not male in F1 family","Error US21 in line 6:Gender of wife with I2 id is not female in F1 family"])

        result=userstory_an.us_21([['F',4],['F',6],'F1','I1','I2'])
        self.assertEqual(result,["Error US21 in line 4:Gender of husband with I1 id is not male in F1 family",0])

        result=userstory_an.us_21([['M',4],['M',6],'F1','I1','I2'])
        self.assertEqual(result,[0,"Error US21 in line 6:Gender of wife with I2 id is not female in F1 family"])

        result=userstory_an.us_21([['NA',-1],['M',6],'F1','NA','I2'])
        self.assertEqual(result,[0,"Error US21 in line 6:Gender of wife with I2 id is not female in F1 family"])

        result=userstory_an.us_21([['F',4],['NA',-1],'F1','I1','NA'])
        self.assertEqual(result,["Error US21 in line 4:Gender of husband with I1 id is not male in F1 family",0])

        result=userstory_an.us_21([['NA',-1],['NA',-1],'F1','NA','NA'])
        self.assertEqual(result,[0,0])

if __name__=='__main__':
    unittest.main()