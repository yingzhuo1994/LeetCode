# 1st solution
# O(n) time | O(n) space
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False for _ in range(n)]
        visited[source] = True
        stack = deque([source])
        while stack:
            node = stack.popleft()
            for dst in graph[node]:
                if not visited[dst]:
                    if dst == destination:
                        return True
                    visited[dst] = True
                    stack.append(dst)
        return visited[destination]