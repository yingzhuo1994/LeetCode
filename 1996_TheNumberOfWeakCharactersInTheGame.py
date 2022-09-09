# 1st solution, TLE
# O(n^2) time | O(1) space
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        n = len(properties)
        visited = set()
        for i in range(n):
            for j in range(i + 1, n):
                if i not in visited and all(properties[i][k] < properties[j][k] for k in range(2)):
                    visited.add(i)
                if j not in visited and all(properties[i][k] > properties[j][k] for k in range(2)):
                    visited.add(j)
        return len(visited)
