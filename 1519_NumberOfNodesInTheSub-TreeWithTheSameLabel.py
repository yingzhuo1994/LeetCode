# 1st solution
# O(n) time | O(n) space
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        alphabet = string.ascii_lowercase
        dic = {i: {ch: 0 for ch in alphabet} for i in range(n)}

        def dfs(node, parent):
            for neigh in graph[node]:
                if neigh != parent:
                    dfs(neigh, node)
                    for ch in alphabet:
                        dic[node][ch] += dic[neigh][ch]
            dic[node][labels[node]] += 1
        
        dfs(0, -1)
        ans = [dic[i][labels[i]] for i in range(n)]
        return ans