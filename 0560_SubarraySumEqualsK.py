# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = [0] + nums
        for i in range(1, len(dp)):
            dp[i] += dp[i - 1]
        count = 0
        for i in range(1, len(dp)):
            for j in range(i):
                if dp[i] - dp[j] == k:
                    count += 1
        return count

# 2nd solution, TLE
# O(n^2) time | O(1) space
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    count += 1
        return count

# 3rd solution, hash map
# O(n) time | O(n) space
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        dic = {0: 1}
        for i in range(len(nums)):
            total += nums[i]
            if total - k in dic:
                count += dic[total - k]
            dic[total] = dic.get(total, 0) + 1
        return count