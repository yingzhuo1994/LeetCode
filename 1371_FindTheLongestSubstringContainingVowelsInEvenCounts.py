# 1st solution
# O(n) time | O(1) space
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {ch: i for i, ch in enumerate("aeiou")}
        mask = 0
        dic = {0: -1}
        ans = 0
        for i, ch in enumerate(s):
            if ch in vowels:
                mask ^= (1 << vowels[ch])
                if mask not in dic:
                    dic[mask] = i
            ans = max(ans, i - dic[mask])
        return ans