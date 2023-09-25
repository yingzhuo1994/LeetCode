# 1st solution
# O(3^n) time | O(3^n) space
class Solution:
    def checkValidString(self, s: str) -> bool:
        left = s.count("(")
        right = s.count(")")
        star = s.count("*")
        if abs(left - right) > star:
            return False
        
        @cache
        def dfs(idx, total):
            if idx == len(s):
                return total == 0
            if total < 0:
                return False
            if s[idx] == "(":
                return dfs(idx + 1, total + 1)
            elif s[idx] == ")":
                return dfs(idx + 1, total - 1)
            else:
                return dfs(idx + 1, total + 1) or dfs(idx + 1, total - 1) or dfs(idx + 1, total)
        
        return dfs(0, 0)