# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        dic = Counter(nums)
        minVal, maxVal = min(nums), max(nums)
        diff = maxVal - minVal
        if diff <= n - 1:
            return n - len(dic)
        else:
            nums.sort()
            ans = n
            for i, num in enumerate(nums):
                idx = bisect.bisect_left(nums, num + n)
                valid = len(set(nums[i:idx]))
                ans = min(ans, n - valid)
                if idx == n:
                    break
            return ans