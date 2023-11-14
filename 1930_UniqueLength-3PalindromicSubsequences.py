# 1st solution
# O(n) time | O(n) space
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set()
        dic = {}
        for i, ch in enumerate(s):
            if ch not in dic:
                dic[ch] = []
            dic[ch].append(i)
        print(dic)
        for ch in dic:
            if len(dic[ch]) < 2:
                continue
            start = dic[ch][0] + 1
            end = dic[ch][-1] - 1
            for i in range(start, end + 1):
                new = ch + s[i] + ch
                # print(new)
                ans.add(new)
        return len(ans)
            