# 1st solution
# O(3^n) time | O(3^n) space
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def helper(s1, s2):
            if (s1, s2) in memo:
                return memo[(s1, s2)]

            if len(s1) == 1:
                return s1 == s2
            elif s1 == s2:
                return True
            elif Counter(s1) != Counter(s2):
                return False

            for i in range(1, len(s1)):
                if helper(s1[:i], s2[-i:]) and helper(s1[i:], s2[:-i]) or \
                helper(s1[:i], s2[:i]) and helper(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
            memo[(s1, s2)] = False
            return False
        memo = {}
        return helper(s1, s2)