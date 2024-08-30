# 1st solution
# O(kn) time | O(1) space
# where k is the digit number
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        k = len(str(nums[0]))
        n = len(nums)
        ans = 0
        for i in range(k):
            dp = [0] * 10
            for num in nums:
                d = num // pow(10, i) % 10
                dp[d] += 1
            for val in dp:
                ans += val * (n - val)
        return ans // 2