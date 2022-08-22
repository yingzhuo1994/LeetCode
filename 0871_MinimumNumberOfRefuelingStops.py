# 1st solution
# O(2^n) time | O(2^n) space
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:       
        stations.append([target, 0])
        stack = [[0, startFuel, 0]]
        for position, fuel in stations:
            newStack = []
            for curPosition, leftFuel, stop in stack:
                if curPosition + leftFuel >= position:
                    newStack.append([curPosition, leftFuel, stop])
                    newStack.append([position, leftFuel - (position - curPosition) + fuel, stop + 1])
            stack = newStack
            if not stack:
                return -1
        ans = float("inf")
        for curPosition, leftFuel, stop in stack:
            if curPosition + leftFuel >= target:
                ans = min(ans, stop)
        return ans

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxDistance = startFuel
        minStack = []
        stops = 0
        stations.append([target, 0])
        for position, fuel in stations:
            while minStack and maxDistance < position:
                maxDistance -= heappop(minStack)
                stops += 1
            if maxDistance < position:
                return -1
            heappush(minStack, -fuel)
        return stops
