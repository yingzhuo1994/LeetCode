# 1st solution
# O(kn) time | O(kn) space
# k = 5
class Solution:
    def countVowelStrings(self, n: int) -> int:
        @lru_cache(None)
        def helper(number, start):
            if number == 0:
                return 0
            if start > 5:
                return 0
            if number == 1:
                return 5 - start + 1
            
            count = 0
            for v in range(start, 6):
                count += helper(number - 1, v)
            return count 
        return helper(n, 1)

# 2nd solution
# O(1) time | O(1) space
import math
class Solution:
    def countVowelStrings(self, n: int) -> int:
        k = 5
        return math.factorial(n + k - 1) // (math.factorial(k - 1) * math.factorial(n))