# 1st solution
# O(n) time | O(1) space
class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = -1
        start = 0
        diff = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                if diff == 0 or diff == -1:
                    ans = max(ans, i - start + 1)
                else:
                    start = i - 1
                diff = 1
            elif nums[i] - nums[i-1] == -1:
                if diff == 1:
                    ans = max(ans, i - start + 1)
                    diff = -1
                else:
                    start = i
                    diff = 0
            else:
                start = i
                diff = 0
        return ans