# 1st solution
# O(5^n) time | O(n) space
class Solution:
    def countVowelStrings(self, n: int) -> int:
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