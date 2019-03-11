import unittest
from userstories_an import *

class testcase(unittest.TestCase):

    def test_07(self):
        result=userstory_an.us_07([['1996-10-21',4],['2150-10-21',6],154,'I1'])
        self.assertEqual(result,"Error US07 in line 4 or line 6:Age of person is 150 years with I1 id")

        result=userstory_an.us_07(['NA',['1994-04-03',6],'NA','I1'])
        self.assertEqual(result,0)

        result=userstory_an.us_07([['1994-06-12',4],'NA',154,'I1'])
        self.assertEqual(result,"Error US07 in line 4:Age of person is 150 years with I1 id")

        result=userstory_an.us_07(['NA','NA','NA','I1'])
        self.assertEqual(result,0)

        result=userstory_an.us_07(['NA',['Invalid',9],'NA','I1'])
        self.assertEqual(result,0)

        result=userstory_an.us_07([['Invalid',7],['Invalid',9],'Invalid','I1'])
        self.assertEqual(result,0)

        result=userstory_an.us_07([['1994-06-12',4],['Invalid',8],'Invalid','I1'])
        self.assertEqual(result,0)

        result=userstory_an.us_07([['1947-04-15',4],['1900-04-15',6],-47,'I1'])
        self.assertEqual(result,0)

if __name__=='__main__':
    unittest.main()