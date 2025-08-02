# 1st solution
# O(n) time | O(1) space
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = {}
        valid = 0
        ans = 0
        start = 0
        for i, ch in enumerate(s):
            dic[ch] = dic.get(ch, 0) + 1
            if dic[ch] == 1:
                valid += 1
            while valid == 3:
                dic[s[start]] -= 1
                if dic[s[start]] == 0:
                    valid -= 1
                start += 1
            else:
                ans += start
        return ans