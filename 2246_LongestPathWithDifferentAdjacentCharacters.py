# 1st solution
# O(n) time | O(n) space
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = [[] for _ in range(n)]
        for i, p in enumerate(parent):
            if p == -1:
                continue
            graph[p].append(i)

        def dfs(node, parent):
            print(node, parent)
            maxLength = 1
            first, second = 0, 0
            for neig in graph[node]:
                if neig == parent:
                    continue 
                a, b = dfs(neig, node)
                maxLength = max(maxLength, b)
                if s[node] != s[neig]:
                    if a >= first:
                        first, second = a, first
                    elif a >= second:
                        second = a
            endAtNode = first + 1
            maxLength = max(maxLength, first + 1 + second)
            return endAtNode, maxLength
        
        _, ans = dfs(0, -1)
        return ans