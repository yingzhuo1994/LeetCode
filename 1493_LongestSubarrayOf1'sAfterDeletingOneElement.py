# 1st solution
# O(n) time | O(n) space
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        ones = sum(nums)
        zeroes = n - ones
        if zeroes == 0:
            return ones - 1
        elif zeroes == 1:
            return ones
        
        dp = []
        i = 0
        while i < n:
            if nums[i] == 0:
                dp.append(0)
                i += 1
            else:
                start = i
                while i < n and nums[i] == 1:
                    i += 1
                dp.append(i - start)
        dp.append(0)
        ans = 0
        for i in range(len(dp) - 1):
            if dp[i] == 0:
                val = dp[i-1] + dp[i + 1]
                ans = max(ans, val)
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        ones = sum(nums)
        zeroes = n - ones
        if zeroes == 0:
            return ones - 1
        elif zeroes == 1:
            return ones
        
        ans = 0
        left = 0
        i = 0
        while i < n:
            if nums[i] == 0:
                i += 1
            start = i
            while i < n and nums[i] == 1:
                i += 1
            right = i - start
            ans = max(ans, left + right)
            left = right

        return ans