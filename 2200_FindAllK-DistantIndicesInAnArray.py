# 1st solution
# O(n) time | O(1) space
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = [-1]
        for i, num in enumerate(nums):
            if num == key:
                for j in range(max(ans[-1] + 1, i - k), min(len(nums), i + k + 1)):
                    ans.append(j)
        return ans[1:]