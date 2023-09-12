# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        
        @cache
        def dfs(a, b):
            for node in graph[a]:
                if node == b:
                    return True
                if dfs(node, b):
                    return True
            return False
        
        ans = [dfs(a, b) for a, b in queries]

        return ans