# 1st solution, TLE
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        length = len(s)
        while length > 0:
            stringSet = set()
            for i in range(len(s)-length + 1):
                string = s[i:i+length]
                if string in stringSet:
                    return string
                stringSet.add(string)
            length -= 1
        return ""

# 2nd solution, MLE
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        trie = Trie(s)
        print(trie.dic)
        result = ""
        for i in range(1, len(s)):
            string = s[i:]
            cur = trie.add(string)
            if len(cur) > len(result):
                result = cur
        return result
    

class Trie:
    def __init__(self, s):
        self.dic = {}
        dic = self.dic
        for ch in s:
            dic = dic.setdefault(ch, {})

    def add(self, s):
        dic = self.dic
        path = ""
        for ch in s:
            if ch in dic:
                path += ch
            dic = dic.setdefault(ch, {})
        return path

# 3rd solution
# O（n*log(n))
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        beg, end = 0, len(s)
        q = (1 << 31) - 1 
        Found = ""
        while beg + 1 < end:
            mid = (beg + end) // 2
            isFound, candidate = self.RabinKarp(s, mid, q)
            if isFound:
                beg, Found = mid, candidate
            else:
                end = mid

        return Found

    def RabinKarp(self, text, M, q):
        if M == 0: return True
        h, t, d = (1 << (8 * M - 8)) % q, 0, 256

        dic = defaultdict(list)

        for i in range(M): 
            t = (d * t + ord(text[i]))% q

        dic[t].append(i - M + 1)

        for i in range(len(text) - M):
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            for j in dic[t]:
                if text[i + 1:i + M + 1] == text[j:j + M]:
                    return (True, text[j:j + M])
            dic[t].append(i + 1)
        return (False, "")

# 4th solution
# O（n*log(n)) | O(n) space
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        A = [ord(ch) - ord('a') for ch in s]
        mod = 2**63 - 1

        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(s)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen: return i - L + 1
                seen.add(cur)
        res, lo, hi = 0, 0, len(s)

        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return s[res:res + lo]