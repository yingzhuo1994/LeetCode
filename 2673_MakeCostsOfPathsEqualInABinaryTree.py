# 1st solution
# O(n) time | O(n) space
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        paths = [0 for _ in range(n)]
        def dfs(node, total):
            if node >= n + 1:
                return
            left = 2 * node
            right = 2 * node + 1
            total += cost[node - 1]
            paths[node - 1] = total
            if left <= n:
                dfs(left, total)
            if right <= n:
                dfs(right, total)
        
        dfs(1, 0)
        h = int(math.log2(n + 1))
        start = pow(2, h - 1)
        end = n
        level = paths[start - 1:]
        total = max(level)
        level = [total - num for num in level]
        ans = 0
        while len(level) > 1:
            newLevel = []
            for i in range(0, len(level), 2):
                lower = min(level[i:i+2])
                newLevel.append(lower)
                ans += max(level[i:i+2]) - lower
            level = newLevel
        return ans