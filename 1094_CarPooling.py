# 1st solution
# O(nlog(n)) time | O(n) space
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda v: v[1])
        hp = []
        for num, src, dst in trips:
            while hp and hp[0][0] <= src:
                n = hp[0][1]
                heapq.heappop(hp)
                capacity += n
            capacity -= num
            heapq.heappush(hp, [dst, num])
            if capacity < 0:
                return False
        return True
