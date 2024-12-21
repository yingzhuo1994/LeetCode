# 1st solution
# O(m + n) time | O(m + n) space
# where m = len(edges)
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        degrees = [0 for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degrees[a] += 1
            degrees[b] += 1
        
        ans = 0
        level = deque([node for node in range(n) if degrees[node] == 1])
        count = 0
        while level:
            node = level.popleft()
            if degrees[node] == 0:
                continue
            if values[node] % k == 0:
                ans += 1
            else:
                for neig in graph[node]:
                    values[neig] += values[node]
            for neig in graph[node]:
                degrees[neig] -= 1
                if degrees[neig] == 1:
                    level.append(neig)
            values[node] = 0
            degrees[node] = 0
            count += 1
        ans += n - count
        return ans