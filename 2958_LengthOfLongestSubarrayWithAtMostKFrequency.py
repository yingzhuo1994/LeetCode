# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dic = {}
        start = 0
        ans = 0
        for i, num in enumerate(nums):
            dic[num] = dic.get(num, 0) + 1
            if dic[num] <= k:
                ans = max(ans, i - start + 1)
            while dic[num] > k:
                dic[nums[start]] -= 1
                start += 1
        return ans