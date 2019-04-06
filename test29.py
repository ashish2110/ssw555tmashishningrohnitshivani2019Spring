import unittest
import io
import sys
from us_ny import us29_list_dead

class TestProject(unittest.TestCase):
    def test_us29_list_dead(self):
        # Redirect stdout for unit test
        capturedOutput = io.StringIO()               
        sys.stdout = capturedOutput
        # case 1:if input is empty, function should not break 
        test_ind = {}
        us29_list_dead(test_ind)
        self.assertEqual(capturedOutput.getvalue(), '\nUS29: List all deceased individuals:\n')
        # case 2: input contains deceased and function should print tuplet
        test_ind = {"@I1@": {'NAME': ['Sherley /Johnson/', 17], 'DEAT_DATE': ['Invalid', 25], 'ALIVE': 'False'}}
        us29_list_dead(test_ind)
        self.assertIn('Sherley /Johnson/', capturedOutput.getvalue())
        # case 3: input does not contain deceased and function should not print tuplet
        test_ind = {"@I3@": {'NAME': ['Christine /Clie/', 40],  'DEAT_DATE': 'NA', 'ALIVE': 'True'}}
        self.assertNotIn('@I3@', capturedOutput.getvalue())
        # case 4: input lacks of 'ALIVE' attribute and function should not print tuplet
        test_ind = {"@I2@":  {'NAME': ['Smith /Johnson/', 28], 'BIRT_DATE': ['1976-05-10', 34], 'DEAT_DATE': ['2005-06-10', 36]}}
        us29_list_dead(test_ind)
        self.assertNotIn('@I2@', capturedOutput.getvalue())
        # case 5: input contains multiple deceased and function should print all
        test_ind = {'@I7@': {'NAME': ['David /Johnson/', 79], 'DEAT_DATE': ['1995-05-10', 87], 'ALIVE': 'False'},
                    '@I8@': {'NAME': ['Benjamin /Bing/', 91], 'DEAT_DATE': ['2019-03-15', 99], 'ALIVE': 'False'}           
        }
        us29_list_dead(test_ind)
        self.assertIn('@I7@', capturedOutput.getvalue())
        self.assertIn('@I8@', capturedOutput.getvalue())
        # Reset redirection
        sys.stdout = sys.__stdout__
         

if __name__ == '__main__':
    unittest.main()