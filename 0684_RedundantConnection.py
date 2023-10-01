# 1st solution
# O(n) time | O(n) space
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = [[] for _ in range(n+1)]
        dic = {}
        count = [0 for _ in range(n+1)]
        for i, (a, b) in enumerate(edges):
            print(i, a, b)
            graph[a].append(b)
            graph[b].append(a)
            count[a] += 1
            count[b] += 1
            dic[(a, b)] = i
        
        leaves = [node for node in range(1, n + 1) if count[node] == 1]
        visited = set(leaves)

        while leaves:
            new = []
            for leaf in leaves:
                for neig in graph[leaf]:
                    if neig not in visited:
                        count[neig] -= 1
                        if count[neig] == 1:
                            new.append(neig)
                            visited.add(neig)
            leaves = new

        ans = -1
        for node in range(1, n + 1):
            if node not in visited:
                for neig in graph[node]:
                    if neig not in visited:
                        # print(node, neig)
                        if (node, neig) in dic:
                            ans = max(ans, dic[(node, neig)])
                        else:
                            ans = max(ans, dic[(neig, node)])
        
        return edges[ans]


