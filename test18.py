import unittest
import io
import sys
from us_ny import us18_sibling_marriage

class TestProject(unittest.TestCase):
    def test_us18_sibling_marriage(self):
        # Redirect stdout for unit test
        capturedOutput = io.StringIO()               
        sys.stdout = capturedOutput

        test_fam = {
            '@F1@': {'HUSB': ['@I11@', 153], 'WIFE': ['@I12@', 154], 'CHIL': [['@I1@', 155], ['@I2@', 156]]},
            '@F2@': {'HUSB': ['@I1@', 253], 'WIFE': ['@I2@', 254], 'CHIL': [['@I21@', 255]]},
            '@F3@': {'HUSB': ['@I13@', 353], 'WIFE': ['@I14@', 354], 'CHIL': [['@I3@', 355]]},
            '@F4@': {'HUSB': ['@I15@', 453], 'WIFE': ['@I14@', 454], 'CHIL': [['@I4@', 455]]},
            '@F5@': {'HUSB': ['@I3@', 553], 'WIFE': ['@I4@', 554], 'CHIL': [['@I22@', 555]]},
            '@F6@': {'HUSB': ['@I16@', 653], 'WIFE': ['@I17@', 654], 'CHIL': [['@I5@', 655]]},
            '@F7@': {'HUSB': ['@I16@', 753], 'WIFE': ['@I18@', 754], 'CHIL': [['@I6@', 755]]},
            '@F8@': {'HUSB': ['@I5@', 853], 'WIFE': ['@I6@', 854], 'CHIL': [['@I23@', 855]]},
            '@F9@': {'HUSB': ['@I7@', 953], 'WIFE': ['@I8@', 954], 'CHIL': [['@I24@', 955]]}
        }
        us18_sibling_marriage(test_fam)
        # case 1: couple has the same mother and father
        self.assertIn('@I1@', capturedOutput.getvalue())
        self.assertIn('@I2@', capturedOutput.getvalue())
        # case 2: couple has the same mother only
        self.assertIn('@I3@', capturedOutput.getvalue())
        self.assertIn('@I4@', capturedOutput.getvalue())
        # case 3: couple has the same father only
        self.assertIn('@I5@', capturedOutput.getvalue())
        self.assertIn('@I6@', capturedOutput.getvalue())
        # case 4: couple does not share mother or father
        self.assertNotIn('@I7@', capturedOutput.getvalue())
        self.assertNotIn('@I8@', capturedOutput.getvalue())
        # Reset redirection
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()