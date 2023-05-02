# 1st solution
# O(n) time | O(1) space
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                ans *= -1
        
        return ans