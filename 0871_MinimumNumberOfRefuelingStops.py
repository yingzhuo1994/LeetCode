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
        maxPosition = startFuel
        stop = 0
        minStack = []
        i = 0
        while maxPosition < target:
            while i < len(stations) and stations[i][0] <= maxPosition:
                heappush(minStack, -stations[i][1])
                i += 1

            if minStack:
                gas = -heappop(minStack)
                maxPosition += gas
                stop += 1
            else:
                return -1
        
        if maxPosition >= target:
            return stop
        else:
            return -1
