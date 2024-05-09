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
            if alice < plants[i]:
                alice = capacityA
                count += 1
            alice -= plants[i]
            if bob < plants[n-1-i]:
                bob = capacityB
                count += 1
            bob -= plants[n-1-i]
        
        if n & 1 and max(alice, bob) < plants[n // 2]:
            count += 1

        return count