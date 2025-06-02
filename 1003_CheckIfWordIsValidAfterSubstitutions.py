# 1st solution
class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        if len(s) < 3:
            return False
        idx = s.find("abc")
        if idx < 0:
            return False
        return self.isValid(s[:idx] + s[idx+3:])