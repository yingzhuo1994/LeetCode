# O(n) time | O(1) space
class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        def getTrend(diff):
            if diff > 0:
                return 1
            elif diff < 0:
                return -1
            else:
                return 0
            
        n = len(temperatureA)
        ans = 0
        count = 0
        for i in range(n - 1):
            diff1 = temperatureA[i+1] - temperatureA[i]
            diff2 = temperatureB[i+1] - temperatureB[i]
            a = getTrend(diff1)
            b = getTrend(diff2)
            if a == b:
                count += 1
            else:
                count = 0
            ans = max(ans, count)
        return ans