# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        if max(nums) >= target:
            return 1
        n = len(nums)
        dp = [0]
        for i in range(n):
            dp.append(dp[-1] + nums[i])
        
        def isValid(k):
            for i in range(n-k+1):
                if dp[i+k] - dp[i] >= target:
                    return True
            return False

        left, right = 1, n
        ans = n
        while left < right:
            mid = left + (right - left) // 2
            if isValid(mid):
                ans = min(ans, mid)
                right = mid
            else:
                left = mid + 1
        return ans

# 2nd solution
# O(n * log(n)) time | O(1) space
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        if max(nums) >= target:
            return 1
        n = len(nums)
        for i in range(n-1):
            nums[i+1] += nums[i]
        nums.append(0)
        ans = n
        for start in range(n):
            i = bisect.bisect_left(nums, nums[start-1] + target, lo=start, hi=n)
            if i == start or i == n:
                continue
            ans = min(ans, i - start+1)
        return ans