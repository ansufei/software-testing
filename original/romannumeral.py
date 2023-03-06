import re

class RomanNumeral:
    
    def __init__(self):
        self.map = {'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000}
        self.map_order = ['I','V','X','L','C','D','M']

    def validCharacters(self, s):
        return not any(i for i in s if i not in self.map.keys())
    
    def validCombination(self, s):
        # check there are no more than 3 consecutive identical characters (and no more than 1 if 50 or 500)
        pattern = r'[a-zA-Z]{2,}'
        # check that the next character is allowed (must be immediately above or below current number
        # - skip 50 and 500 when checking for other digits)
        return True
    
    
    def convert(self, s):
        if self.validCharacters(s) and self.validCombination(s):
            convertedNumber = 0
            for index, i in enumerate(s):
                currentNumber = self.map[i]
                next = 0
                if index + 1 < len(s):
                    next = self.map[s[index+1]]
                if currentNumber >= next:
                    convertedNumber += currentNumber
                else:
                    convertedNumber -= currentNumber
            return convertedNumber
        else:
            print('Invalid numeral')
            return 'Invalid numeral'
    
sol = RomanNumeral()

# The code above will produce errors as soon as there are more than 2 characters in the number
# (or even on some choices of characters, like LL, which doesn't exist)
# we should test for numbers > 2 characters
sol.convert('B')
# we should test for invalid numbers
#sol.convert('IXCLI')
# sol.convert('IIII)
# sol.convert('LL)
# or numbers that aren't in the dictionary at all should return a proper error code, e.g.
#sol.convert('IVB')
# both addition and subtraction e.g. IXI