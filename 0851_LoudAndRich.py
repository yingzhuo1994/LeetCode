# 1st solution
# O(n) time | O(n) space
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in quiet]
        for a, b in richer:
            graph[b].append(a)
        
        @cache
        def dfs(node):
            ans = node
            for child in graph[node]:
                temp = dfs(child)
                if quiet[ans] > quiet[temp]:
                    ans = temp
            return ans
        
        return [dfs(i) for i in range(n)]