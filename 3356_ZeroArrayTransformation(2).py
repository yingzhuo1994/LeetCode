# 1st solution, TLE
# O(nq) time | O(1) space
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        zeros = sum(num == 0 for num in nums)
        n = len(nums)
        if zeros == n:
            return 0
        for i, query in enumerate(queries, 1):
            l, r, val = query
            for j in range(l, r + 1):
                if nums[j] > 0:
                    nums[j] = max(0, nums[j] - val)
                    if nums[j] == 0:
                        zeros += 1
            if zeros == n:
                return i
        return -1