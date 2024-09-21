# 1st solution
# O(n) time | O(n) space
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        points = [0] * n
        for i, v in enumerate(edges):
            points[v] += i
        ans = -1
        val = 0
        for i, v in enumerate(points):
            if v > val:
                ans = i
                val = v
        return ans