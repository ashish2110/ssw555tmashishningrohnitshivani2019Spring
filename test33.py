import unittest
from userstories_an import *

class testcase(unittest.TestCase):

    def test_33(self):
        result=userstory_an.us_33([['1994-06-12',4],['1994-04-03',6],17,'I1'])
        self.assertEqual(result,'I1')

        result=userstory_an.us_33([['1994-06-12',4],['1994-04-03',6],19,'I1'])
        self.assertEqual(result,0)

        result=userstory_an.us_33([['1994-06-12',4],['Invalid',6],17,'I1'])
        self.assertEqual(result,0)


        result=userstory_an.us_33([['Invalid',4],['1994-04-03',6],17,'I1'])
        self.assertEqual(result,0)
        

        result=userstory_an.us_33([['Invalid',4],['Invalid',6],17,'I1'])
        self.assertEqual(result,0)

        result=userstory_an.us_33(['NA',['1994-04-03',6],17,'I1'])
        self.assertEqual(result,0)

        result=userstory_an.us_33([['1994-06-12',4],'NA',17,'I1'])
        self.assertEqual(result,0)

        result=userstory_an.us_33(['NA','NA',17,'I1'])
        self.assertEqual(result,0)


if __name__=='__main__':
    unittest.main()