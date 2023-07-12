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