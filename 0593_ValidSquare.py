# 1st solution
# O(1) time | O(1) space
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def cal_dist(A, B):
            return (A[0] - B[0])**2 + (A[1] - B[1])**2
        
        def get_vector(A, B):
            dx = B[0] - A[0]
            dy = B[1] - A[1]
            return [dx, dy]
        
        def is_vertical(A, B):
            return A[0] * B[0] + A[1] * B[1] == 0

        points = [p1, p2, p3, p4]
        points.sort()
        dist1 = cal_dist(points[0], points[3])
        dist2 = cal_dist(points[1], points[2])
        if dist1 != dist2 or dist1 == 0:
            return False
        
        v1 = get_vector(points[0], points[1])
        v2 = get_vector(points[0], points[2])
        dist3 = cal_dist(points[0], points[1])
        dist4 = cal_dist(points[0], points[2])
        
        return is_vertical(v1, v2) and dist3 == dist4 and dist3 > 0