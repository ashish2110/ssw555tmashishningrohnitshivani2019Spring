import unittest
import io
import sys
from us_ny import us30_list_living_married

class TestProject(unittest.TestCase):
    def test_us30_list_living_married(self):
        # Redirect stdout for unit test
        capturedOutput = io.StringIO()               
        sys.stdout = capturedOutput

        test_ind = {
            '@I1@': {'NAME': ['Case /1/', 17], 'FAMS': 'NA', 'ALIVE': 'False'},
            '@I2@': {'NAME': ['Case /2/', 27], 'FAMS': 'NA', 'ALIVE': 'True'},
            '@I3@': {'NAME': ['Case /3/', 37], 'FAMS': [['@F1@', 35]], 'ALIVE': 'False'},
            '@I4@': {'NAME': ['Case /4/', 47],  'FAMS': [['@F1@', 45]], 'ALIVE': 'True'},
        }
        test_fam = {
            '@F1@': {'HUSB': ['@I3@', 153], 'WIFE': ['@I4@', 154], 'CHIL': [['@I1@', 155]]}
        }

        us30_list_living_married(test_ind, test_fam)
        
        # case 1: individual not married and not alive
        self.assertNotIn('@I1@', capturedOutput.getvalue())
        # case 2: individual alive but not married
        self.assertNotIn('@I2@', capturedOutput.getvalue())
        # case 3: individual married but not alive
        self.assertNotIn('@I3@', capturedOutput.getvalue())
        # case 4: individual alive and married
        self.assertIn('@I4@', capturedOutput.getvalue())

        # Reset redirection
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()