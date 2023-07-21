# 1st solution
# O(n^2) time | O(n) space 
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = [dp[j][0] + 1, dp[j][1]]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
        
        dic = {}
        for length, count in dp:
            dic[length] = dic.get(length, 0) + count
        
        maxLnegth = max(dic.keys())
        return dic[maxLnegth]
