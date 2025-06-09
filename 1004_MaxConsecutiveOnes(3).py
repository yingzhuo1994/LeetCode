# 1st solution
# O(n) time | O(1) space
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt = [0, 0]
        start = 0
        for i, num in enumerate(nums):
            cnt[num] += 1
            if k < cnt[0]:
                cnt[nums[start]] -= 1
                start += 1
        return len(nums) - start
