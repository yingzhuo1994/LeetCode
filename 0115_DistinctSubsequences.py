class Solution:
    # 1st solution, TLE
    def numDistinct(self, s: str, t: str) -> int:
        if not t:
            return 1
        
        count = 0
        for i in range(len(s)):
            if s[i] == t[0]:
                count += self.numDistinct(s[i + 1:], t[1:])
        return count