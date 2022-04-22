# 1st solution, TLE
from collections import defaultdict


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
# O（n*log(n)) | O(n) space
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        A = [ord(ch) - ord('a') for ch in s]
        mod = 2**63 - 1

        def test(L):
            p = pow(26, L, mod)
            hashValue = reduce(lambda x, y: (x * 26 + y) % mod, A[:L])
            seen = defaultdict(list)
            seen[hashValue].append(0)
            for i in range(L, len(s)):
                hashValue = (hashValue * 26 + A[i] - A[i - L] * p) % mod
                if hashValue in seen:
                    for start in seen[hashValue]:
                        if A[start:start + L] == A[i - L + 1: i + 1]:
                            return i - L + 1
                seen[hashValue].append(i - L + 1)
            return None
        res, low, high = 0, 0, len(s)

        while low < high:
            mid = (low + high + 1) // 2
            pos = test(mid)
            if pos is not None:
                low = mid
                res = pos
            else:
                high = mid - 1
        return s[res:res + low]