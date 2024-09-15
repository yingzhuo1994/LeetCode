# 1st solution
# O(kn) time | O(n) space
# where k = len(nums), n = 100
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = [False] * 100
        for a, b in nums:
            points[a:b+1] = [True] * (b - a + 1)
        return sum(points)