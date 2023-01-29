# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        for i, num in enumerate(nums):
            isFound = False
            for j in range(i + 1, n):
                if nums[j] > num:
                    ans[i] = nums[j]
                    isFound = True
                    break
            if isFound:
                continue
            for j in range(i):
                if nums[j] > num:
                    ans[i] = nums[j]
                    break
        return ans