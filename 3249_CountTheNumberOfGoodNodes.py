# 1st solution
# O(n) time | O(n) space
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        self.ans = 0
        def dfs(node, prev=None):
            lst = []
            for neig in graph[node]:
                if neig == prev:
                    continue
                lst.append(dfs(neig, node))
            if not lst or len(set(lst)) == 1:
                # print(node)
                self.ans += 1
            return sum(lst) + 1 
        
        dfs(0)
        return self.ans