# 1st solution
# O(mn) time | O(n) space
# where m = len(trips)
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def findPath(x: int, fa: int, end: int) -> bool:
            if x == end:
                cnt[x] += 1
                return True  # 找到 end
            for y in graph[x]:
                if y != fa and findPath(y, x, end):
                    cnt[x] += 1  # x 是 end 的祖先节点，也就在路径上
                    return True
            return False  # 未找到 end
        
        cnt = [0] * n
        for start, end in trips:
            findPath(start, -1, end)

        # 类似 337. 打家劫舍 III
        def dfs(x: int, fa: int) -> (int, int):
            not_halve = price[x] * cnt[x]  # x 不变
            halve = not_halve // 2  # x 减半
            for y in graph[x]:
                if y != fa:
                    nh, h = dfs(y, x)  # 计算 y 不变/减半的最小价值总和
                    not_halve += min(nh, h)  # x 不变，那么 y 可以不变或者减半，取这两种情况的最小值
                    halve += nh  # x 减半，那么 y 只能不变
            return not_halve, halve
        
        return min(dfs(0, -1))