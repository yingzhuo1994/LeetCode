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

# 2nd solution
# O(m) time | O(m) space
# where m is the maximum distance
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        m = max([i for _,_,i in trips])
        times = [0]*(m+2)
        for i,j,k in trips:
            times[j+1] += i
            times[k+1] -= i
        return all(num <= capacity for num in accumulate(times))