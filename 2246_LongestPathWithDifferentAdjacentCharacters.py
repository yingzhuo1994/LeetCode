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

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        children = [[] for i in range(len(s))]
        for i,j in enumerate(parent):
            if j >= 0:
                children[j].append(i)
        
        res = [0]
        def dfs(i):
            candi = [0]
            for j in children[i]:
                cur = dfs(j)
                if s[i] != s[j]:
                    candi.append(cur)
                    
            candi = nlargest(2, candi)
            res[0] = max(res[0], sum(candi) + 1)
            return max(candi) + 1
        
        dfs(0)
        return res[0]