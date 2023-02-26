# 1st solution
# O(n * 2^n) time | O(2^n) space
class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [False] * (n + 1)
        memo = {}
        def dfs(idx, visited):
            key = tuple(visited)
            if key in memo:
                return memo[key]
            if idx == n + 1:
                return 1
            count = 0
            for v in range(1, len(visited)):
                if not visited[v]:
                    if v % idx == 0 or idx % v == 0:
                        visited[v] = True
                        count += dfs(idx + 1, visited)
                        visited[v] = False
            memo[key] = count
            return count
                      
        return dfs(1, visited)