# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = [[num, i] for i, num in enumerate(arr)]
        nums.sort()
        n = len(arr)
        ans = [-1 for _ in range(n)]
        rank = 0
        for idx in range(n):
            num, i = nums[idx]
            if idx > 0 and num == nums[idx - 1][0]:
                ans[i] = rank
            else:
                rank += 1
                ans[i] = rank
        return ans