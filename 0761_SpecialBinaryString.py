# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        cur, last = 0, 0
        ret = []
        for i in range(len(s)):
            cur += 1 if s[i] == '1' else -1
            if cur == 0:
                ret.append('1' + self.makeLargestSpecial(s[last + 1 : i]) + '0')
                last = i + 1
        return ''.join(sorted(ret, reverse=True))