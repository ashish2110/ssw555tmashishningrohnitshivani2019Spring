import unittest
import io
import sys
from main import Gedcom

class TestProject(unittest.TestCase):
    def test_us27_ind_age(self):
        # Redirect stdout for unit test
        capturedOutput = io.StringIO()               
        sys.stdout = capturedOutput

        FILENAME="My-Family-27-Jan-2019-275.ged"
        gedcom = Gedcom(FILENAME)
        gedcom.print_gedcom()
        # case of invalid date
        self.assertIn('2019-04-20 | Invalid', capturedOutput.getvalue())
        # case of person alive
        self.assertIn('1980-04-08 |    39', capturedOutput.getvalue())
        # case of person dead
        self.assertIn('1950-04-07 |    20   | False | 1970-12-20', capturedOutput.getvalue())
        # case of dead before birth / negative value
        self.assertIn('2004-05-08 |    -1   | False | 2003-03-15', capturedOutput.getvalue())

        # Reset redirection
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()