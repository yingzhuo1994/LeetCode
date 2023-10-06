# 1st solution
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def containsCycle(node, visited):
            if node in visited:
                return True
            visited.add(node)
            for neig in graph[node]:
                if containsCycle(neig, visited):
                    return True
            visited.remove(node)
            return False
        
        n = len(edges)
        graph = {i: [] for i in range(1, n + 1)}
        inCount = {i: 0 for i in range(1, n + 1)}
        edgeIndex = {}
        for i in range(n):
            a, b = edges[i]
            edgeIndex[(a, b)] = i
            graph[a].append(b)
            inCount[b] += 1
        
        root = None
        for i in range(1, n + 1):
            if inCount[i] == 0:
                root = i
                break
        
        if root is None:
            candidates = [node for node in range(1, n + 1) if inCount[node] == 1]
            for node in candidates:
                visited = set()
                if containsCycle(node, visited):
                    break
            ans = None
            maxIdx = -1
            for node in visited:
                for neig in graph[node]:
                    if neig in visited and edgeIndex[(node, neig)] > maxIdx:
                        ans = [node, neig]
                        maxIdx = edgeIndex[(node, neig)]

            return ans
        
        ansNode = 0
        for node in range(1, n + 1):
            if inCount[node] == 2:
                ansNode = node
                break
        
        visited = set()
        if containsCycle(ansNode, visited):
            for node in visited:
                if (node, ansNode) in edgeIndex:
                    return [node, ansNode]

        for a, b in reversed(edges):
            if b == ansNode:
                return [a, b]

# 2nd solution
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(ds, i):
            if ds[i] == 0:
                return i
            else:
                ds[i] = find(ds, ds[i])
                return ds[i]

        n = len(edges)
        parent = [-1 for _ in range(n + 1)]
        ds = [0 for _ in range(n + 1)]

        first = -1
        second = -1
        last = -1

        for i in range(n):
            p, c = edges[i]
            if parent[c] != -1:
                first = parent[c]
                second = i
                continue

            parent[c] = i
            
            p1 = find(ds, p)

            if p1 == c:
                last = i
            else:
                ds[c] = p1

        if last == -1:
            return edges[second] # no cycle found by removing second
        if second == -1:
            return edges[last] # no edge removed
    
        return edges[first]