# 1st solution
# O(1) time | O(1) space
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        w1 = ax2 - ax1
        h1 = ay2 - ay1
        s1 = w1 * h1

        w2 = bx2 - bx1
        h2 = by2 - by1
        s2 = w2 * h2

        # calculate x overlap
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        x_overlap = max(0, right - left)

        # calculate y overlap
        top = min(ay2, by2)
        bottom = max(ay1, by1)
        y_overlap = max(0, top - bottom)

        area_of_overlap = 0
        # if the rectangles overlap each other, then calculate
        # the area of the overlap

        area_of_overlap = x_overlap * y_overlap

        # area_of_overlap is counted twice when in the summation of
        # area_of_a and area_of_b, so we need to subtract it from the
        # total, to get the toal area covered by both the rectangles
        total_area = s1 + s2 - area_of_overlap

        return total_area
