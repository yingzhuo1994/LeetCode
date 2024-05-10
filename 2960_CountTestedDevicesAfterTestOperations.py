# 1st solution
# O(n) time | O(1) space
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n = len(batteryPercentages)
        count = 0
        for i in range(n):
            battery = max(0, batteryPercentages[i] - count)
            if battery > 0:
                count += 1
        return count