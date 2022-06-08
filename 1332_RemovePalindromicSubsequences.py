# 1st solution
# O(n) time | O(n) space
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        else:
            return 2

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return 2
            left += 1
            right -= 1
        return 1