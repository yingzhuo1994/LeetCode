# 1st solution
# O(n) time | O(1) space
class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            color = rings[i]
            loc = int(rings[i + 1])
            rods[loc].add(color)
        
        ans = 0
        for rod in rods:
            if len(rod) == 3:
                ans += 1
        return ans