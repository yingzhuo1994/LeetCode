# 1st solution
# O(n) time | O(n) space
class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        s = [0] * len(nextVisit)
        for i, j in enumerate(nextVisit[:-1]):
            s[i + 1] = (s[i] * 2 - s[j] + 2) % 1_000_000_007
        return s[-1]