# 1st solution
# O(n) time | O(1) space
class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for length in range(1, n + 1):
            if n % length != 0:
                continue
            t = "".join(sorted(s[:length]))
            valid = True
            for i in range(length, n, length):
                t1 = "".join(sorted(s[i:i+length]))
                if t != t1:
                    valid = False
                    break
            if valid:
                return len(t)
        return n
