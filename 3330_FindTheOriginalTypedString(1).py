# 1st solution
# O(n) time | O(1) space
class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = len(word)
        last = word[0]
        for ch in word:
            if ch != last:
                ans -= 1
                last = ch
        return ans


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def possibleStringCount(self, s: str) -> int:
        return len(s) - len(list(groupby(s))) + 1