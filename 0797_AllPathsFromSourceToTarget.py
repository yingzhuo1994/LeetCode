# 1st solution
# O(n) time | O(n) space
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        self.visited = set()
        self.dfs(graph, 0, len(graph) - 1, [])
        return self.result

    def dfs(self, graph, current, goal, path):
        if current == goal:
            path.append(current)
            self.result.append(path)
            return 
        path.append(current)
        self.visited.add(current)
        for node in graph[current]:
            if node not in self.visited:
                self.dfs(graph, node, goal, path[:])
        self.visited.remove(current)
