# 1st solution, TLE
# O(mn) time | O(mn) space
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        def traverse(i, j):
            if i < 0:
                return
            if j < len(nums[i]):
                ans.append(nums[i][j])
            traverse(i - 1, j + 1)
            
        m = len(nums)
        n = max(map(len, nums))
        ans = []
        for i in range(m):
            traverse(i, 0)
        
        for j in range(1, n):
            traverse(m - 1, j)
        return ans