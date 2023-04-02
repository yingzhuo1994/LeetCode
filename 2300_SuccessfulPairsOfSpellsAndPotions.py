# 1st solution
# O(m*log(m) + n*log(m)) time | O(n) space
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(spells)
        m = len(potions)
        ans = [0 for _ in range(n)]
        for i, num in enumerate(spells):
            target = (success - 1) // spells[i] + 1
            idx = bisect.bisect_left(potions, target)
            ans[i] = m - idx
        return ans