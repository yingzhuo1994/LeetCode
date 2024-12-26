# 1st solution
# O(n) time | O(1) space
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        vis = set()
        for x, y in pairwise(s):
            vis.add(x + y)
            if y + x in vis:
                return True
        return False