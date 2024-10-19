# 1st solution
# O(n) time | O(1) space
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op = 0
        ans = 0
        for num in nums:
            if num ^ op:
                continue
            op ^= 1
            ans += 1
        return ans