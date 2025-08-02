# 1st solution
# O(n) time | O(1) space
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            if len(str(num)) & 1:
                continue
            ans += 1
        return ans