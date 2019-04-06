import unittest
import io
import sys
from us_ny import us26_match_entries

class TestProject(unittest.TestCase):
    def test_us26_match_entries(self):
        # Redirect stdout for unit test
        capturedOutput = io.StringIO()               
        sys.stdout = capturedOutput
        test_ind = {
            '@I1@': {'NAME': ['Case /1/', 17], 'FAMC': [['@F11@', 26]], 'FAMS': 'NA'},
            '@I2@': {'NAME': ['Case /2/', 27], 'FAMC': [['@F1@', 36]], 'FAMS': 'NA'},
            '@I3@': {'NAME': ['Case /3/', 37], 'FAMC': 'None', 'FAMS': [['@F12@', 35]]},
            '@I4@': {'NAME': ['Case /4/', 47], 'FAMC': 'None', 'FAMS': [['@F2@', 45]]},
            '@I5@': {'NAME': ['Case /8/', 57], 'FAMC': [['@F3@', 46]], 'FAMS': 'NA'},
            '@I6@': {'NAME': ['Case /9/', 67], 'FAMC': [['@F6@', 56]], 'FAMS': 'NA'},
            '@I7@': {'NAME': ['Case /9/', 77], 'FAMC': 'None', 'FAMS': [['@F6@', 55]]},
            '@I8@': {'NAME': ['Case /9/', 87], 'FAMC': 'None', 'FAMS': [['@F6@', 65]]}
        }
        test_fam = {
            '@F1@': {'HUSB': ['@I12@', 153], 'WIFE': ['@I13@', 154], 'CHIL': [['@I1@', 155]]},
            '@F2@': {'HUSB': ['@I2@', 253], 'WIFE': ['@I3@', 254], 'CHIL': [['@I21@', 255]]},
            '@F3@': {'HUSB': ['@I1@', 353], 'WIFE': ['@I4@', 354], 'CHIL': [['@I22@', 355]]},
            '@F4@': {'HUSB': ['@I14@', 453], 'WIFE': ['@I15@', 454], 'CHIL': [['@I23@', 455]]},
            '@F5@': {'HUSB': ['@I16@', 553], 'WIFE': ['@I17@', 554], 'CHIL': [['@I5@', 555]]},
            '@F6@': {'HUSB': ['@I7@', 653], 'WIFE': ['@I8@', 654], 'CHIL': [['@I6@', 655]]}
        }
        us26_match_entries(test_ind, test_fam)
        # case 1: individual does not have child entry in families
        self.assertIn('@I1@', capturedOutput.getvalue())
        self.assertIn('@F11@', capturedOutput.getvalue())
        # case 2: individual does not match child entry in families
        self.assertIn('@I2@', capturedOutput.getvalue())
        self.assertIn('@F1@', capturedOutput.getvalue())
        # case 3: individual does not have spouse entry in families
        self.assertIn('@I3@', capturedOutput.getvalue())
        self.assertIn('@F12@', capturedOutput.getvalue())
        # case 4: individual does not match spouse entry in families
        self.assertIn('@I4@', capturedOutput.getvalue())
        self.assertIn('@F2@', capturedOutput.getvalue())
        # case 5: family spouse does not have entry in individuals
        self.assertIn('@I12@', capturedOutput.getvalue())
        self.assertIn('@I13@', capturedOutput.getvalue())
        # case 6: family spouse does not match entry in individuals
        self.assertIn('@F3@', capturedOutput.getvalue())
        # case 7: family child does not have entry in individuals
        self.assertIn('@F4@', capturedOutput.getvalue())
        self.assertIn('@I23@', capturedOutput.getvalue())
        # case 8: family child does not match entry in individuals
        self.assertIn('@F5@', capturedOutput.getvalue())
        self.assertIn('@I5@', capturedOutput.getvalue())
        # case 9: individual and family match
        self.assertNotIn('@F6@', capturedOutput.getvalue())
        self.assertNotIn('@I6@', capturedOutput.getvalue())
        self.assertNotIn('@I7@', capturedOutput.getvalue())
        self.assertNotIn('@I8@', capturedOutput.getvalue())
        # Reset redirection
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()