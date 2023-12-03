# 1st solution
# O(n) time | O(1) space
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def calculateDist(A, B):
            if B[0] < A[0]:
                A, B = B, A
            dx = B[0] - A[0]
            dy = abs(B[1] - A[1])
            return max(dx, dy)
        ans = 0
        for i in range(len(points) - 1):
            ans += calculateDist(points[i], points[i + 1])
        return ans