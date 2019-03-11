import unittest
from us_rs import us_rs 
from main import Gedcom


class TestCase(unittest.TestCase):
    
    
    gedcom = Gedcom("My-Family-27-Jan-2019-275.ged")
    fam = gedcom.storeFam()
    ind = gedcom.storeInd()

    
    
    def test_checkLineNumber(self):
        
        self.assertTrue(us_rs.divorceBeforeDeath(self.ind, self.fam))

if __name__ == "__main__":
    unittest.main()