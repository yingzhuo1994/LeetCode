# 1st solution
# O(n) time | O(n) space
import itertools
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        prefixSum = list(itertools.accumulate(distance, initial=0))
        if start > destination:
            start, destination = destination, start
        dist1 = prefixSum[destination] - prefixSum[start]
        dist2 = prefixSum[-1] - dist1
        return min(dist1, dist2)