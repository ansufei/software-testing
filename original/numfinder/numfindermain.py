from numfinder import NumFinder

class NumFinderMain:

    def main(self, nums):
        nf = NumFinder()
        nf.find(nums)
        
        print(nf.getLargest())
        print(nf.getSmallest())


if __name__ == '__main__':
    test = NumFinderMain()
    test.main([4, 25, 7, 9])
    test.main([4, 3, 2, 1])
    test.main([])
