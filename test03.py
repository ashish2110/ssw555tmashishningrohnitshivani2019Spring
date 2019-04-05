import unittest
from userstories_an import *

class testcase(unittest.TestCase):

    def test_03(self):
        result=userstory_an.us_03([['2020-06-12',4],'NA',-2,'I1'])
        self.assertEqual(result,"Error US03 in line 4: Birth date is after death date for person with idI1")

        result=userstory_an.us_03([['1994-06-12',4],['2014-04-03',6],19,'I1'])
        self.assertEqual(result,0)

        result=userstory_an.us_03([['2014-04-03',4],['1994-06-12',6],-19,'I1'])
        self.assertEqual(result,"Error US03 in line 4 or line 6: Birth date is after death date for person with idI1")

        result=userstory_an.us_03([['1994-06-12',4],['Invalid',6],'Invalid','I1'])
        self.assertEqual(result,0)


        result=userstory_an.us_03([['Invalid',4],['1994-04-03',6],'Invalid','I1'])
        self.assertEqual(result,0)
        

        result=userstory_an.us_03([['Invalid',4],['Invalid',6],'Invalid','I1'])
        self.assertEqual(result,0)

        result=userstory_an.us_03(['NA',['1994-04-03',6],'NA','I1'])
        self.assertEqual(result,0)

        result=userstory_an.us_03([['1994-06-12',4],'NA',24,'I1'])
        self.assertEqual(result,0)

        result=userstory_an.us_03(['NA','NA','NA','I1'])
        self.assertEqual(result,0)


if __name__=='__main__':
    unittest.main()