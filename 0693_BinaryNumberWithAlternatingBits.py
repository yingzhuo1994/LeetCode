class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = str(bin(n))[2:]
        last = s[0]
        for i in range(1, len(s)):
            if s[i] == last:
                return False
            last = s[i]
        return True

