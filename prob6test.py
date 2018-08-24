
from prob6 import anagram
import unittest

class KnownValues(unittest.TestCase):
    known_values = (("abcde","bczah",4),("aabcde","bczah",5))

    def test_to_roman_known_values(self):
        '''to_roman should give known result with known input'''
        for nume,numeral,integer in self.known_values:
            result = anagram(nume,numeral)
            self.assertEqual(integer, result)

if __name__ == '__main__':
    unittest.main()

