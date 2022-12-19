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
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        def inBetween(p, i, q):
            a = i[0] >= p[0] and i[0] <= q[0] or i[0] <= p[0] and i[0] >= q[0]
            b = i[1] >= p[1] and i[1] <= q[1] or i[1] <= p[1] and i[1] >= q[1]
            return a and b


        hull = set()
        n = len(trees)
        if n < 4:
            for point in trees:
                x, y = point
                hull.add((x, y))
            return [[x, y] for x, y in hull]

        left_most = 0
        for i in range(n):
            if trees[i][0] < trees[left_most][0]:
                left_most = i
        p = left_most
        while True:
            q = (p + 1) % n
            for i in range(n):
                x, y = trees[i]
                if (x, y) in hull:
                    continue
                if orientation(trees[p], trees[i], trees[q]) < 0:
                    q = i
            for i in range(n):
                x, y = trees[i]
                if i != p and i != q and orientation(trees[p], trees[i], trees[q]) == 0 and inBetween(trees[p], trees[i], trees[q]):
                    hull.add((x, y))
            x, y = trees[q]
            hull.add((x, y))
            p = q
            if p == left_most:
                break
        return [[x, y] for x, y in hull]