# 1st solution
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        # create graph
        for x, y in prerequisites:
            graph[x].append(y)
        # visit each node
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        # mark as being visited
        visited[i] = -1
        # visit all the neighbours
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        return True
    
# 2nd solution
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        inStack = [False for _ in range(numCourses)]
        # create graph
        for a, b in prerequisites:
            graph[b].append(a)
        
        for node in range(numCourses):
            if visited[node]:
                continue

            containsCycle = self.isNodeInCycle(graph, node, visited, inStack)
            if containsCycle:
                return False
        return True
        
    def isNodeInCycle(self, graph, node, visited, inStack):
        visited[node] = True
        inStack[node] = True

        neighbours = graph[node]
        for neighbour in neighbours:
            if not visited[neighbour]:
                containsCycle = self.isNodeInCycle(graph, neighbour, visited, inStack)
                if containsCycle:
                    return True
            elif inStack[neighbour]:
                return True

        inStack[node] = False
        return False
    
# 3rd solution
# O（E + V) time | O(E) space
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE, GREY, BLACK = 0, 1, 2
        graph = [[] for _ in range(numCourses)]
        colors = [WHITE for _ in range(numCourses)]
        # create graph
        for a, b in prerequisites:
            graph[b].append(a) 
        
        for node in range(numCourses):
            if colors[node] != WHITE:
                continue

            containsCycle = self.traverseAndColorNodes(graph, colors, node)
            if containsCycle:
                return False
            
        return True
    
    def traverseAndColorNodes(self, graph, colors, node):
        WHITE, GREY, BLACK = 0, 1, 2
        colors[node] = GREY

        neighbours = graph[node]
        for neighbour in neighbours:
            neighbourColor = colors[neighbour]

            if neighbourColor == GREY:
                return True
            
            if neighbourColor != WHITE:
                continue

            containsCycle = self.traverseAndColorNodes(graph, colors, neighbour)
            if containsCycle:
                return True
        
        colors[node] = BLACK
        return False

