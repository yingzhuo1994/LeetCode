# 1st solution, BFS
# O(n) time | O(n) space
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graphForward = [[] for _ in range(n)]
        graphBackward = [[] for _ in range(n)]

        for a, b in connections:
            graphForward[a].append(b)
            graphBackward[b].append(a)
        
        ans = 0
        level = [0]
        visited = set([0])

        while level:
            newLevel = []
            for node in level:
                while graphForward[node]:
                    neig = graphBackward[node].pop()
                    if neig not in visited:
                        visited.add(neig)
                        ans += 1
                    newLevel.append(neig)
                for neig in graphBackward[node]:
                    if neig not in visited:
                        visited.add(neig)
                        newLevel.append(neig) 
                        
            level = newLevel
        
        return ans

# 2nd solution, DFS
# O(n) time | O(n) space
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graphForward = [[] for _ in range(n)]
        graphBackward = [[] for _ in range(n)]

        for a, b in connections:
            graphForward[a].append(b)
            graphBackward[b].append(a)
        
        self.ans = 0
        visited = [0 for _ in range(n)]

        def dfs(start):
            visited[start] = 1
            for neib in graphForward[start]:
                if visited[neib] == 0:
                    self.ans += 1
                dfs(neib)
            
            for neib in graphBackward[start]:
                if visited[neib] == 0:
                    dfs(neib)
            
        dfs(0)

        return self.ans