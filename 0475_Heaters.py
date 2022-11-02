# 1st solution
# O(m * log(m) + n * log(n) + m * log(k)) time | O(max(m, n)) space
# where k is the largest place
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        m = len(houses)
        n = len(heaters)
        def isValid(r):
            i, j = 0, 0
            while i < m and j < n:
                if abs(houses[i] - heaters[j]) <= r:
                    i += 1
                elif houses[i] > heaters[j] + r:
                    j += 1
                else:
                    return False
            return i >= m
                
        left, right = 0, max(houses[-1], heaters[-1])
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if isValid(mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans

# 2nd solution
# O(n * log(n) + m * log(n)) time | O(n) space
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        r = 0
        for h in houses:
            ind = bisect.bisect_left(heaters, h)
            if ind == len(heaters):
                r = max(r, h - heaters[-1])
            elif ind == 0:
                r = max(r, heaters[0] - h)
            else:
                r = max(r, min(heaters[ind] - h, h - heaters[ind - 1]))
        return r