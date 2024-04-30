# 1st solution, TLE
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask = 0
        lst = [0]
        for i, ch in enumerate(word):
            mask ^= 1 << (ord(ch) - ord("a"))
            lst.append(mask)
        ans = 0
        for i in range(1, len(word) + 1):
            for j in range(i):
                val = lst[i] - lst[j]
                count = val.bit_count()
                if count <= 1:
                    ans += 1
        return ans