# 1st solution
# O(n) time | O(1) space
class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 0
        last = word[0]
        cnt = 0
        for ch in word:
            if ch == last:
                cnt += 1
            else:
                ans += cnt - 1
                cnt = 1
                last = ch
        ans += cnt - 1
        return ans + 1


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def possibleStringCount(self, s: str) -> int:
        return len(s) - len(list(groupby(s))) + 1