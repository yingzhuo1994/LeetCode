# 1st solution
# O(n) time | O(n) space
import itertools
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        prefixSum = list(itertools.accumulate(distance, initial=0))
        dist1 = prefixSum[destination] - prefixSum[start]
        dist2 = prefixSum[-1] - dist1
        return min(dist1, dist2)

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        dist = 0
        dist_start = dist_end = 0
        for i, d in enumerate(distance):
            if i == start:
                dist_start = dist
            elif i == destination:
                dist_end = dist
            dist += d
        dist1 = dist_end - dist_start
        dist2 = dist - dist1
        return min(dist1, dist2)