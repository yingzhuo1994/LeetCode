# 1st solution
# O(mn) time | O(mn) space
# where m and n are the length of s1 and s2, separately
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}
        def dfs(i, j, k):
            if k == len(s3):
                return True
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i + 1, j, k + 1):
                    memo[(i+1, j, k+1)] = True
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j + 1, k + 1):
                    memo[(i, j+1, k+1)] = True
                    return True

            memo[(i, j, k)] = False
            return False
        
        return dfs(0, 0, 0)

# 2nd solution, DP
# O(mn) time | O(mn) space
# where m and n are the length of s1 and s2, separately
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1] or dp[i-1][j] and s1[i-1] == s3[i+j-1]
        return dp[-1][-1]