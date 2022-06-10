# 1st solution, dfs TLE
# O(2^n) time | O(n) space
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ans = 0
        def dfs(i, curSum):
            if i == len(nums):
                if curSum == target:
                    self.ans += 1
                return
            
            dfs(i + 1, curSum + nums[i])
            dfs(i + 1, curSum - nums[i])
        dfs(0, 0)
        return self.ans

# 2nd solution, bfs
# O(2^n) time | O(2^n) space
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dic = {0: 1}
        for num in nums:
            newDic = {}
            for k, v in dic.items():
                curSum = k + num
                newDic[curSum] = newDic.get(curSum, 0) + v
                curSum = k - num
                newDic[curSum] = newDic.get(curSum, 0) + v
            dic = newDic
        return dic.get(target, 0)