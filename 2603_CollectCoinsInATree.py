
# 1st solution
# O(n) time | O(n) space
class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = defaultdict(list)
        degree = [0] * n

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            degree[x] += 1
            degree[y] += 1
        
        rest = n
        # 删除树中所有无金币的叶子节点，直到树中所有的叶子节点都是含有金币的
        q = deque(i for i in range(n) if degree[i] == 1 and coins[i] == 0)
        while q:
            u = q.popleft()
            degree[u] -= 1
            rest -= 1
            for v in g[u]:
                degree[v] -= 1
                if degree[v] == 1 and coins[v] == 0:
                    q.append(v)
        
        # 删除树中所有的叶子节点, 连续删除2次
        for _ in range(2):
            q = deque(i for i in range(n) if degree[i] == 1)
            while q:
                u = q.popleft()
                degree[u] -= 1
                rest -= 1
                for v in g[u]:
                    degree[v] -= 1
        
        return 0 if rest == 0 else (rest - 1) * 2
