# 1st solution, TLE
# O(n^3) time | O(n) space
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        numSet = set(nums)
        for i in range(n - 1):
            a = nums[i]
            for j in range(i + 2, n - 1):
                c = nums[j]
                for k in range(i + 1, j):
                    b = nums[k]
                    product = b * c
                    # print(a, b, c)
                    if product % a != 0:
                        continue
                    target = product // a
                    if target in numSet:
                        ans += 8
                    # print(ans)
        return ans