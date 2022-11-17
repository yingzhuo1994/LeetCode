# 1st solution
# O(1) time | O(1) space
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        if ax1 > bx1:
            ax1, bx1 = bx1, ax1
            ax2, bx2 = bx2, ax2
            ay1, by1 = by1, ay1
            ay2, by2 = by2, ay2

        w1 = ax2 - ax1
        h1 = ay2 - ay1
        s1 = w1 * h1

        w2 = bx2 - bx1
        h2 = by2 - by1
        s2 = w2 * h2

        if bx2 <= ax2 and ay1 <= by1 <= by2 <= ay2:
            return max(s1, s2)

        s = s1 + s2
        
        if bx1 >= ax2 or by2 <= ay1 or by1 >= ay2:
            return s
        

        dx = min(bx2, ax2) - bx1

        if ay1 <= by1 <= by2 <= ay2:
            dy = h2
        elif ay1 <= by2 <= ay2 and by1 <= ay1:
            dy = by2 - ay1
        elif ay1 <= by1 <= ay2 and by2 >= ay2:
            dy = ay2 - by1
        else:
            dy = h1
        ds = dx * dy
        s -= ds
        return s
