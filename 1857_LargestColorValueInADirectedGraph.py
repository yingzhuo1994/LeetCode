# 1st solution, TLE
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
        
        self.ans = -1
        visited = [False for _ in range(n)]
        def dfs(node, count):
            if visited[node]:
                return True
            visited[node] = True
            count[colors[node]] += 1

            for neig in graph[node]:
                containsCycle = dfs(neig, count)
                if containsCycle:
                    return True
            self.ans = max(self.ans, max(list(count.values()) + [-1]))
            
            visited[node] = False
            count[colors[node]] -= 1
            
            return False
        
        for i in range(n):
            containsCycle = dfs(i, Counter())
            if containsCycle:
                return -1
            
        
        return self.ans