# 1st solution
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        maxi = 10 ** n   # store the value of 10ⁿ 
        for z in range(2, maxi): # since both x, y > 0 and z = x + y; which implies that z has a minimum value of 2
            left = maxi - z
            right = int(str(left)[::-1]) # reverese number
            
            discriminant = z ** 2 - 4 * right # b² - 4ac
            if discriminant < 0: # no root
                continue
            else: # there exists at least one real solution; so calculate the roots
                root_1 = (z + discriminant ** 0.5) / 2
                root_2 = (z - discriminant ** 0.5) / 2
                if root_1.is_integer() or root_2.is_integer():
                    return (maxi * left + right) % 1337

# 2nd solution
class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        
        hi, lo = 10**n -1, 10**(n-1)
        top = (hi // 11) * 11
        
        for left in range(hi, lo-1, -1):
            res = int(str(left) + str(left)[::-1])
            
            for d in range(top, left -1, -11):
                if res % d == 0:
                    q = res // d
                    
                    if lo <= q <= hi:
                        return res % 1337