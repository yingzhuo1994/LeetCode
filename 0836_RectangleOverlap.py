# 1st solution
# O(1) time | O(1) space
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] >= rec2[2] or rec1[2] <= rec2[0] or rec1[1] >= rec2[3] or rec1[3] <= rec2[1]:
            return False
        return True