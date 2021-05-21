class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        while start < len(gas):
            i = start
            gasVol = gas[i]
            while gasVol >= cost[i]:
                gasVol -= cost[i]
                if i < len(gas) - 1:
                    i += 1
                else:
                    i = 0
                gasVol += gas[i]
                if i == start:
                    return i
            start += 1
        return -1