# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        alice = capacityA
        bob = capacityB
        count = 0
        half = n // 2
        for i in range(half):
            if alice >= plants[i]:
                alice -= plants[i]
            else:
                alice = capacityA - plants[i]
                count += 1
            if bob >= plants[n-1-i]:
                bob -= plants[n-1-i]
            else:
                bob = capacityB - plants[n-1-i]
                count += 1
        if n & 1:
            if alice >= bob:
                if alice < plants[n // 2]:
                    count += 1
            else:
                if bob < plants[n // 2]:
                    count += 1
        return count