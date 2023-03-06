from original.romannumeral import RomanNumeral
import unittest

class RomanNumeralTest(unittest.TestCase):

    def setUp(self):
        self.roman = RomanNumeral()
    
    def test_singleNumber(self):
        result = self.roman.convert('I')
        self.assertEqual(1, result)
    
    def test_numberWithManyDigits(self):
        result = self.roman.convert('VIII')
        self.assertEqual(8, result)

    def test_numberWithSubtractiveNotation(self):
        result = self.roman.convert('IV')
        self.assertEqual(4, result) 

    # def test_invalidNumeral(self):
    #     result = self.roman.convert('IIII')
    #     self.assertEqual('Invalid numeral', result)

if __name__ == '__main__':
    unittest.main()