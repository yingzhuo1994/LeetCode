# 1st solution
# O(n * log(U)) time | O(n * log(U)) space
class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        @cache 
        def dfs(node: int, idx: int, parent: int) -> int:
            res1 = (coins[node] >> idx) - k
            res2 = coins[node] >> (idx + 1)
            for ch in graph[node]:
                if ch != parent:
                    res1 += dfs(ch, idx, node)  # 不右移
                    if idx < 13:  # idx + 1 >= 14 相当于 res2 += 0，无需递归
                        res2 += dfs(ch, idx + 1, node)  # 右移
            return max(res1, res2)

        return dfs(0, 0, -1)