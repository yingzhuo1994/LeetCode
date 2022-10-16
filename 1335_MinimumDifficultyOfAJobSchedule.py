# 1st solution
# O(kn^2) time | O(kn) space
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
       
        @cache
        def dfs(start, k):
            if k == 0:
                return max(jobDifficulty[start:])
            elif n - start == k + 1:
                return sum(jobDifficulty[start:])
            elif n - start < k + 1:
                return float("inf")
            
            diff = -1
            ans = float("inf")
            for i in range(start, n - k):
                diff = max(diff, jobDifficulty[i])
                ans = min(ans, dfs(i+1, k-1) + diff)
            
            return ans
        
        ans = dfs(0, d - 1)
        return ans if ans != float("inf") else -1

# 2nd solution
# O(kn^2) time | O(kn) space
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        dp = [[float("inf") for _ in range(n)] for _ in range(d)]
        for k in range(d):
            for i in range(n - k):
                if k == 0:
                    dp[k][i] = max(jobDifficulty[i:])
                    continue

                diff = -1
                ans = float("inf")
                for j in range(i, n - k):
                    diff = max(diff, jobDifficulty[j])
                    ans = min(ans, dp[k-1][j+1] + diff)
                dp[k][i] = ans

        return dp[d-1][0]