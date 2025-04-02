# 1st solution
# O(n^3) time | O(1) space
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    val = (nums[i] - nums[j]) * nums[k]
                    ans = max(ans, val)
        return ans