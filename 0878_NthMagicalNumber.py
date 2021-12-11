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