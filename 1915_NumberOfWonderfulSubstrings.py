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


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [1] + [0] * 1024
        res = cur = 0
        for ch in word:
            cur ^= 1 << (ord(ch) - ord('a'))
            res += count[cur]
            res += sum(count[cur ^ (1 << i)] for i in range(10))
            count[cur] += 1
        return res