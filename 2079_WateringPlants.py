# 1st solution
# O(n) time | O(1) space
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        water = capacity
        for i, plant in enumerate(plants):
            if water >= plant:
                water -= plant
                ans += 1
            else:
                water = capacity - plant
                ans += (i + 1) * 2 - 1
        return ans