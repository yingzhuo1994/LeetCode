# 1st solution
# O(n) time | O(n) space
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inCounts = [0 for _ in range(n)]
        for a, b in edges:
            inCounts[b] += 1
        sources = [node for node in range(n) if inCounts[node] == 0]
        if len(sources) != 1:
            return -1
        return sources[0]