# 1st solution
# O(n) time | O(1) space
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for a, b in zip(s, t):
            if a in dic1:
                if dic1[a] != b:
                    return False
            elif b not in dic2:
                dic1[a] = b
                dic2[b] = a
            else:
                return False
        return True