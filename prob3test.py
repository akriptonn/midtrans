from prob3 import norm
import unittest

class KnownValues(unittest.TestCase):
    known_values = (("-","-"),("0","0"),("62","62"),("(null)","(null)"),
                    ("+6281298490805","6281298490805"),
                    ("6281298490805","6281298490805"),
                    ("08119284411","628119284411"),
                    ("+1 (804) 244-3470","18042443470"),
                    ("*083831397998","6283831397998"))

    def test_to_roman_known_values(self):
        '''to_roman should give known result with known input'''
        for nume,numeral in self.known_values:
            result = norm(nume)
            self.assertEqual(numeral, result)

if __name__ == '__main__':
    unittest.main()
