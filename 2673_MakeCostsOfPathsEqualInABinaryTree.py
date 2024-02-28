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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        for i in range(n // 2, 0, -1):  # 从最后一个非叶节点开始算
            ans += abs(cost[i * 2 - 1] - cost[i * 2])  # 两个子节点变成一样的
            cost[i - 1] += max(cost[i * 2 - 1], cost[i * 2])  # 累加路径和
        return ans