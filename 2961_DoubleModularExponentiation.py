# 1st solution
# O(n * log(U)) time | O(1) space
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        return [i for i, (a, b, c, m) in enumerate(variables)
                if pow(pow(a, b, 10), c, m) == target]


# 2nd solution
# O(n * log(U)) time | O(1) space
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        def pow_mod(x, y, z):
            "Calculate (x ** y) % z efficiently."
            res = 1
            while y:
                if y & 1:
                    res = res * x % z
                y >>= 1
                x = x * x % z
            return res
        
        return [i for i, (a, b, c, m) in enumerate(variables)
                if pow_mod(pow_mod(a, b, 10), c, m) == target]