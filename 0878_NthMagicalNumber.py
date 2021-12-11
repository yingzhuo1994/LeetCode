# 1st solution
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        g = self.gcd(a, b)
        largest = a // g * b
        lst = []
        numOne, numTwo = a, b
        while numOne <= largest and numTwo <= largest:
            if numOne < numTwo:
                lst.append(numOne)
                numOne += a
            elif numOne > numTwo:
                lst.append(numTwo)
                numTwo += b
            else:
                lst.append(numOne)
                numOne += a
                numTwo += b

        mod = 10**9 + 7
        k, r = n // len(lst), n % len(lst)
        if r == 0:
            ans = k * lst[-1]
        else:
            ans = k * lst[-1] + lst[r - 1]
        return ans % mod
    
    
    def gcd(self, a, b):
        while a:
            a, b = b % a, a
        return b

# 2nd solution, binary search
# O(log(N*min(a, b))) time | O(1) space
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10 **9 + 7
        g = self.gcd(a, b)
        largest = a // g * b

        def largeEnough(x):
            return x // a + x // b - x // largest >= n
        
        left, right = 0, n * min(a, b)
        while left < right:
            middle = left + (right - left) // 2
            if largeEnough(middle):
                right = middle
            else:
                left = middle + 1

        return left % mod
    
    
    def gcd(self, a, b):
        while a:
            a, b = b % a, a
        return b