# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        inCounts = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[b].append(a)
            inCounts[a] += 1
        
        ans = [[] for _ in range(n)]
        
        @cache
        def getChildren(node):
            if len(graph[node]) == 0:
                return []

            for neig in graph[node]:
                ans[node].extend([neig] + getChildren(neig))
            ans[node] = sorted(list(set(ans[node])))
            return ans[node]
        
        sources = [node for node in range(n) if inCounts[node] == 0]
        for node in sources:
            getChildren(node)
        return ans
        