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

# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt4 = 0
        cnt3 = [0] * len(nums)
        for l in range(2, len(nums)):
            cnt2 = 0
            for j in range(l):
                if nums[j] < nums[l]:  # 3 < 4
                    cnt4 += cnt3[j]
                    # 把 j 当作 i，把 l 当作 k，现在 nums[i] < nums[k]，即 1 < 2
                    cnt2 += 1
                else:  # 把 l 当作 k，现在 nums[j] > nums[k]，即 3 > 2
                    cnt3[j] += cnt2
        return cnt4