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

# 2nd solution
# O(n) time | O(n) space
# n = total num
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                key = i + j
                if key not in dic:
                    dic[key] = []
                dic[key].append(nums[i][j])
        maxIdx = max(dic.keys())
        ans = []
        for i in range(maxIdx + 1):
            ans.extend(dic[i][::-1])
        return ans