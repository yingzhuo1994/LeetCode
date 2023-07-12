# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        end_nodes = [i for i in range(n) if len(graph[i]) == 0]
        visited = set(end_nodes)
        ans = set(end_nodes)
        
        def dfs(node):
            if node in visited:
                return node in ans
            visited.add(node)
            if all(dfs(neig) for neig in graph[node]):
                ans.add(node)
                return True
            else:
                return False
        
        for i in range(n):
            dfs(i)
        
        ans = list(ans)
        ans.sort()
        return ans

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        revGraph = [[] for _ in range(n)]
        outCount = [len(graph[i]) for i in range(n)]
        for node in range(n):
            for neig in graph[node]:
                revGraph[neig].append(node)
        level = [i for i in range(n) if len(graph[i]) == 0]
        ans = [False for _ in range(n)]
        for node in level:
            ans[node] = True
        while level:
            newLevel = []
            for node in level:
                for neig in revGraph[node]:
                    if ans[neig]:
                        continue
                    outCount[neig] -= 1
                    if outCount[neig] == 0:
                        ans[neig] = True
                        newLevel.append(neig)
            level = newLevel
        
        ans = [node for node in range(n) if ans[node]]

        return ans