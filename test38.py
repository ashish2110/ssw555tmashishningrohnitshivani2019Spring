import unittest
from userstories_an import *

class testcase(unittest.TestCase):

    def test_03(self):
        result=userstory_an.us_38([['2020-06-12',4],'NA',-2,'I1',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999)])
        self.assertEqual(result,0)

        result=userstory_an.us_38([['1994-06-12',4],['2014-04-03',6],19,'I1',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999)])
        self.assertEqual(result,0)

        result=userstory_an.us_38([['1994-04-12',4],['2014-04-03',6],19,'I1',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999)])
        self.assertEqual(result,0)

        result=userstory_an.us_38([['2014-04-03',4],['1994-06-12',6],-19,'I1',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999)])
        self.assertEqual(result,0)

        result=userstory_an.us_38([['1994-06-12',4],['Invalid',6],'Invalid','I1',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999)])
        self.assertEqual(result,0)


        result=userstory_an.us_38([['Invalid',4],['1994-04-03',6],'Invalid','I1',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999)])
        self.assertEqual(result,0)
        

        result=userstory_an.us_38([['Invalid',4],['Invalid',6],'Invalid','I1',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999)])
        self.assertEqual(result,0)

        result=userstory_an.us_38(['NA',['1994-04-03',6],'NA','I1',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999)])
        self.assertEqual(result,0)

        result=userstory_an.us_38([['1994-04-12',4],'NA',24,'I1',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999)])
        self.assertEqual(result,'I1')

        result=userstory_an.us_38([['1994-05-02',4],'NA',24,'I1',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999)])
        self.assertEqual(result,'I1')

        result=userstory_an.us_38([['1994-06-02',4],'NA',24,'I1',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999)])
        self.assertEqual(result,0)

        result=userstory_an.us_38(['NA','NA','NA','I1',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999)])
        self.assertEqual(result,0)


if __name__=='__main__':
    unittest.main()