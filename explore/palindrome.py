class Solution:
    def getNumberOfDigits(self, x: int) -> int:
        '''
        question say 2^38 + 1 is maximum possible number and manually counting gives me 10 digits
        so to get the number of digits,
        loop through the range(1 to maxNumberOfDigits)
        right shift the number (by dividing by powers of 10)
        the power of 10 that makes the shifted value less than 1 is the number of digits
        '''
        for i in range(1, 11):
            if x/(10**i) < 1:
                return i

    def getDigitsFromFront(self, x: int) -> int:
        pass

    def getDigitsFromBack(self, x: int) -> int:
        '''
        after getting number of digits
        we can loop through the range (1, number of digits)
        and get a certain position in a number by getting the remainder of

        numberRounded = number%(10^position) - number%(10^(position-1))
        e.g. from 121 we will get, 1, 20 and 100 for position 3,2 & 1 respectively
        before storing those numbers trim them by dividing by 10*(position-1) of number
        e.g. 20/(10^(2-1)) is 2 and 100

        '''
        for i in range(1, self.getNumberOfDigits(x)+1):
            currentNumber = (x%(10**(i)))-x%(10**(i-1))
            if i > 1:
                currentNumber = currentNumber/(10**(i-1)) 
            yield currentNumber

    def rebuildDigitsFromBack(self, x: list) -> int:
        total = 0
        for index, i in enumerate(x):
            total += i * (10**((len(x)-1)-index))
        return total 
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x<10:
            return True
        else:
            digitsFromTheBack = list(self.getDigitsFromBack(x))
            reversedDigits = self.rebuildDigitsFromBack(digitsFromTheBack)
            return(reversedDigits == x)

solution = Solution()
print(solution.isPalindrome(1234567899))
