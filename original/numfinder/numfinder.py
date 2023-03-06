import sys

class NumFinder:
    
    def __init__(self):
        self.smallest = sys.maxsize
        self.largest = - sys.maxsize - 1

    def find(self, nums):
        for n in nums:
            if (n < self.smallest):
                self.smallest = n
            if (n > self.largest):
                self.largest = n
        return self.smallest, self.largest
        
    def getSmallest(self):
        return self.smallest
    
    def getLargest(self):
        return self.largest