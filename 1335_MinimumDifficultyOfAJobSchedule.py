# 1st solution
# O(kn) time | O(kn) space
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