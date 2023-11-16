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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = i = 0
        while i < n:
            if nums[i] > threshold or nums[i] & 1:
                i += 1  # 直接跳过
                continue
            start = i  # 记录这一组的开始位置
            i += 1  # 开始位置已经满足要求，从下一个位置开始判断
            while i < n and nums[i] <= threshold and nums[i] % 2 != nums[i - 1] % 2:
                i += 1
            # 从 start 到 i-1 是满足题目要求的子数组
            ans = max(ans, i - start)
        return ans