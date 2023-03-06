from original.gettingstarted import GettingStarted
import unittest

class GettingStartedTest(unittest.TestCase):
    
    def test_addFiveTo20(self):
        result = GettingStarted().addFive(20)
        self.assertEqual(25, result)
    
    def test_addFiveToZero(self):
        result = GettingStarted().addFive(0)
        self.assertEqual(5, result)

    def test_addFiveToMinus20(self):
        result = GettingStarted().addFive(-20)
        self.assertEqual(-15, result)

if __name__ == '__main__':
    unittest.main()