# 1st solution
class Solution:
    @cache
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        
        ans = float("inf")
        if len(s1) > 0:
            ans = min(ans, ord(s1[0]) + self.minimumDeleteSum(s1[1:], s2))
        if len(s2) > 0:
            ans = min(ans, ord(s2[0]) + self.minimumDeleteSum(s1, s2[1:]))
        if s1 and s2 and s1[0] == s2[0]:
            ans = min(ans, self.minimumDeleteSum(s1[1:], s2[1:]))
        
        return ans

# 2nd solution
# O(n1 * n2) time | O(n1 * n2) space
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def helper(i, j):
            if i == len(s1) and j == len(s2):
                return 0
            elif i == len(s1):
                return sum(ord(s2[k]) for k in range(j, len(s2)))
            elif j == len(s2):
                return sum(ord(s1[k]) for k in range(i, len(s1)))
            else:
                if s1[i] == s2[j]:
                    return helper(i + 1, j + 1)
                else:
                    left = ord(s1[i]) + helper(i + 1, j)
                    right = ord(s2[j]) + helper(i, j + 1)
                    return min(left, right)
        return helper(0, 0)