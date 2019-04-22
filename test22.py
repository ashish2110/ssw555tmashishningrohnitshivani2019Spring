import unittest
import io
import sys
from main import Gedcom

class TestProject(unittest.TestCase):
    def test_us22_unique_id(self):
        # Redirect stdout for unit test
        capturedOutput = io.StringIO()               
        sys.stdout = capturedOutput

        FILENAME="My-Family-27-Jan-2019-275.ged"
        gedcom = Gedcom(FILENAME)
        # Non-unique ID cases
        self.assertIn('ERROR US22 for ID  @F8@', capturedOutput.getvalue())
        self.assertIn('ERROR US22 for ID  @I15@', capturedOutput.getvalue())
        # Unique ID cases
        self.assertNotIn('ERROR US22 for ID  @F3@', capturedOutput.getvalue())
        self.assertNotIn('ERROR US22 for ID  @I2@', capturedOutput.getvalue())
        # Reset redirection
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()