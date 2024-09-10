# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        great = [0] * n
        great[-1] = [0] * (n + 1)
        for k in range(n - 2, 0, -1):
            great[k] = great[k + 1].copy()
            for x in range(1, nums[k + 1]):
                great[k][x] += 1

        ans = 0
        for j in range(1, n - 1):
            for k in range(j + 1, n - 1):
                x = nums[k]
                if nums[j] > x:
                    ans += (x - n + 1 + j + great[j][x]) * great[k][nums[j]]
        return ans