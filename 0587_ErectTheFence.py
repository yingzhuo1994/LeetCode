class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        points = trees
        """Computes the convex hull of a set of 2D points.

        Input: an iterable sequence of (x, y) pairs representing the points.
        Output: a list of vertices of the convex hull in counter-clockwise order,
          starting from the vertex with the lexicographically smallest coordinates.
        Implements Andrew's monotone chain algorithm. O(n log n) complexity.
        """

        # Sort the points lexicographically (tuples are compared lexicographically).
        # Remove duplicates to detect the case we have just one unique point.
        # points = sorted(set(points))
        points = sorted(points, key=lambda p: (p[0], p[1]))

        # Boring case: no points or a single point, possibly repeated multiple times.
        if len(points) <= 1:
            return points

        # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
        # Returns a positive value, if OAB makes a counter-clockwise turn,
        # negative for clockwise turn, and zero if the points are collinear.
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        # Build lower hull
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(p)

        # Build upper hull
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(p)

        # Concatenation of the lower and upper hulls gives the convex hull.
        # Last point of each list is omitted because it is repeated at the
        # beginning of the other list.
        # return lower[:-1] + upper[:-1]
        lst = lower[:-1] + upper[:-1]
        ans = set()
        for x, y in lst:
            ans.add((x, y))
        ans = [[x, y] for x, y in ans]
        return ans

# 2nd solution
# O(n*log(n)) time | O(n) space
class Solution:
    def outerTrees(self, points):
        def cross(p1, p2, p3):
            return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

        start = min(points)
        points.pop(points.index(start))
        points.sort(key=lambda p: (atan2(p[1]-start[1], p[0]-start[0]), -p[1], p[0]))
        
        last = len(points) - 1
        while last > 0 and cross(start, points[-1], points[last - 1]) == 0:
            last -= 1
            
        points[last:] = sorted(points[last:], key = lambda p: (-p[0]))

        ans = [start]
        for p in points:
            ans.append(p)
            while len(ans) > 2 and cross(*ans[-3:]) < 0:
                ans.pop(-2)
        return ans