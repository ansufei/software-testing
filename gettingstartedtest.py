from original.gettingstarted import GettingStarted
#from original import gettingstarted
import unittest

class GettingStartedTest(unittest.TestCase):
    
    def addFiveTo20(self):
        result = GettingStarted().addFive(20)
        self.assertEqual(25, result)
    
    def addFiveToZero(self):
        result = GettingStarted().addFive(0)
        self.assertEqual(5, result)

    def addFiveToMinus20(self):
        result = GettingStarted().addFive(-20)
        self.assertEqual(-15, result)

if __name__ == '__main__':
    unittest.main()