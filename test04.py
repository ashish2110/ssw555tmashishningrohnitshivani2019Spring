import unittest
from userstories_an import *

class testcase(unittest.TestCase):

    def test_04(self):
        result=userstory_an.us_04([['1994-06-12',4],['1994-04-03',6],'F1'])
        self.assertEqual(result,"Error US04 in line 6 or line 4:Marriage date occurs after Divorce date in F1 family")

        result=userstory_an.us_04(['NA',['1994-04-03',6],'F1'])
        self.assertEqual(result,0)

        result=userstory_an.us_04([['1994-06-12',4],'NA','F1'])
        self.assertEqual(result,0)

        result=userstory_an.us_04(['NA','NA','F1'])
        self.assertEqual(result,0)

        result=userstory_an.us_04(['NA',['Invalid',4],'F1'])
        self.assertEqual(result,0)

        result=userstory_an.us_04([['Invalid',6],['Invalid',8],'F1'])
        self.assertEqual(result,0)

        result=userstory_an.us_04([['1994-06-12',4],['Invalid',8],'F1'])
        self.assertEqual(result,0)

        result=userstory_an.us_04([['1977-12-06',4],['1980-12-08',6],'F2'])
        self.assertEqual(result,0)
        
if __name__=='__main__':
    unittest.main()