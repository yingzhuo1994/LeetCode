# 1st solution
# O((E + V) * aV + V * log(V)) time | O(V) space
# V represents the number of vertices (the length of the given string)
# and E represents the number of edges (the number of pairs) 
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        disjointSet = DisjointSet()
        for a, b in pairs:
            disjointSet.add(a, s[a])
            disjointSet.add(b, s[b])
            disjointSet.union(a, b)
        
        stack = list(s)
        for i in range(len(stack)):
            if i not in disjointSet.parent:
                continue
            candidate = ""
            dataSet = disjointSet.getDataSet(i)

            for k in string.ascii_lowercase:
                if dataSet[k] > 0:
                    candidate = k
                    break
                    
            stack[i] = candidate
            dataSet[candidate] -= 1

        return "".join(stack)

class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.dataSet = {}
    
    def add(self, a, ch):
        if a not in self.parent:
            self.parent[a] = a
            self.rank[a] = 1
            self.dataSet[a] = {ch : 0 for ch in string.ascii_lowercase}
            self.dataSet[a][ch] = 1
    
    # make a and b part of the same component
    # union by rank optimization
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb: return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
            for k, v in self.dataSet[pb].items():
                self.dataSet[pa][k] += v
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]
            for k, v in self.dataSet[pa].items():
                self.dataSet[pb][k] += v

    # find the representative of the 
    # path compression optimization
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def getDataSet(self, a):
        parent = self.find(a)
        return self.dataSet[parent]

# 2nd solution
# O(E + V * log(V)) time | O(E + V) space
# V represents the number of vertices (the length of the given string)
# and E represents the number of edges (the number of pairs) 
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Maximum number of vertices
        N = len(s)
        visited = [False for _ in range(N)];
        adj = [[] for _ in range(N)]; 
        
        def DFS(s, vertex, characters, indices):
            # Add the character and index to the list
            characters.append(s[vertex])
            indices.append(vertex)
            
            visited[vertex] = True
            
            # Traverse the adjacents
            for adjacent in adj[vertex]:
                if not visited[adjacent]:
                    DFS(s, adjacent, characters, indices)
        
        # Build the adjacency list
        for source, destination in pairs:
            # Undirected edge
            adj[source].append(destination)
            adj[destination].append(source)
        
        answer = list(s)
        for vertex in range(N):
            # If not covered in the DFS yet
            if not visited[vertex]:
                characters = []
                indices = []
                
                DFS(s, vertex, characters, indices)
                # Sort the list of characters and indices
                characters.sort()
                indices.sort()

                # Store the sorted characters corresponding to the index
                for index in range(len(characters)):
                    answer[indices[index]] = characters[index]
        return "".join(answer)