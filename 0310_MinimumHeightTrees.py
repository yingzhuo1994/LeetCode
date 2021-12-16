# 1st solution, TLE
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        table = collections.defaultdict(dict)

        for a, b in edges:
            table[a][a] = 0
            table[b][b] = 0
            table[a][b] = 1
            table[b][a] = 1
        
        for k in table:
            for a in table[k]:
                for b in table[k]:
                    table[a][b] = min(table[a].get(b, float("inf")), table[a][k] + table[k][b])
        
        heights = []
        for i in range(n):
            if i not in table:
                heights.append(float("inf"))
            else:
                heights.append(max(table[i].values()))
        
        minHeight = min(heights)
        ans = []
        for i in range(n):
            if heights[i] == minHeight:
                ans.append(i)
        
        return ans

# 2nd solution, Topological sorting
# O(V) time | O(V) space
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # base cases
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            # remove the current leaves along with the edges
            while leaves:
                leaf = leaves.pop()
                # the only neighbor left for the leaf node
                neighbor = neighbors[leaf].pop()
                # remove the only edge left
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # prepare for the next round
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph
        return leaves