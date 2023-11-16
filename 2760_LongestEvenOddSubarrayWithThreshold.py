# 1st solution
# O(n) time | O(1) space
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = 0
        start = 0
        while start < len(nums):
            if nums[start] & 1 or nums[start] > threshold:
                start += 1
            else:
                ans = max(ans, 1)
                i = start
                while i < len(nums) - 1:
                    if nums[i] % 2 == nums[i + 1] % 2 or nums[i + 1] > threshold:
                        ans = max(ans, i - start + 1)
                        break
                    elif i == len(nums) - 2:
                        ans = max(ans, len(nums) - start)
                    i += 1
                start = i + 1
        return ans
