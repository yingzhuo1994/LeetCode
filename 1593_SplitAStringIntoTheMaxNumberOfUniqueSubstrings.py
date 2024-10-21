# 1st solution
# O(2^n) time | O(n) space
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        def dfs(idx, visited):
            ans = 0
            for i in range(idx, n):
                sub = s[idx:i+1]
                if sub in visited:
                    continue
                visited.add(sub)
                val = dfs(i + 1, visited)
                ans = max(ans, val + 1)
                visited.remove(sub)
            return ans
        return dfs(0, set())