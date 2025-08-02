# 1st solution
# O(n) time | O(n) space
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        prefixMax = [0] * n
        suffixMin = [float("inf")] * n
        for i in range(n - 1):
            prefixMax[i] = max(prefixMax[i - 1], nums[i])
        for i in reversed(range(1, n)):
            suffixMin[i] = min(suffixMin[(i + 1)%n], nums[i])

        ans = 0
        for i in range(1, n - 1):
            if prefixMax[i - 1] < nums[i] < suffixMin[i + 1]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1
        return ans