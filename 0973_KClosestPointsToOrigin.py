# 1st solution, Max Heap
# O(n*log(k)) time | O(k) space
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for x, y in points:
            dist = x**2 + y**2
            heappush(hp, [-dist, [x, y]])
            if len(hp) > k:
                heappop(hp)
        return [elem[1] for elem in hp]