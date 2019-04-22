import unittest
from userstories_an import *

class testcase(unittest.TestCase):

    def test_39(self):
        result=userstory_an.us_39([['2020-06-12',4],'True','True',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999),'I1','I2'])
        self.assertEqual(result,0)

        result=userstory_an.us_39([['2020-06-12',4],'True','False',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999),'I1','I2'])
        self.assertEqual(result,0)

        result=userstory_an.us_39([['2020-06-12',4],'Fasle','False',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999),'I1','I2'])
        self.assertEqual(result,0)

        result=userstory_an.us_39([['2020-04-27',4],'True','True',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999),'I1','I2'])
        self.assertEqual(result,['I1','I2'])

        result=userstory_an.us_39([['2020-05-04',4],'True','True',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999),'I1','I2'])
        self.assertEqual(result,['I1','I2'])

        result=userstory_an.us_39([['2020-04-27',4],'True','False',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999),'I1','I2'])
        self.assertEqual(result,0)

        result=userstory_an.us_39([['2020-05-04',4],'True','False',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999),'I1','I2'])
        self.assertEqual(result,0)

        result=userstory_an.us_39([['2020-05-03',4],'False','False',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999),'I1','I2'])
        self.assertEqual(result,0)

        result=userstory_an.us_39([['Invalid',4],'False','False',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999),'I1','I2'])
        self.assertEqual(result,0)

        result=userstory_an.us_39(['NA','False','False',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999),'I1','I2'])
        self.assertEqual(result,0)

        result=userstory_an.us_39([['Invalid',4],'True','True',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999),'I1','I2'])
        self.assertEqual(result,0)

        result=userstory_an.us_39(['NA','True','True',datetime.datetime(2019, 4, 5, 12, 10, 10, 870999),'I1','I2'])
        self.assertEqual(result,0)

if __name__=='__main__':
    unittest.main()