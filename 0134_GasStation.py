# 1st solution
# O(n^2) | O(1) space
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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If sum of gas is less than sum of cost, then there is no way to get through all stations.
        # So while we loop through the stations we sum up, so that at the end we can check the sum.
        # Otherwise, there must be one unique solution, so the first one I find is the right one. 
        # If the tank becomes negative, we restart because that can't happen.
        if sum(gas) < sum(cost):
            return -1
        
        gas_tank, start_index = 0, 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i + 1
                gas_tank = 0
            
        return start_index