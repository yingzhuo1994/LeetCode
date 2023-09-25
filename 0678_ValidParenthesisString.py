# 1st solution
# O(n^#) time | O(n^2) space
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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = cmax = 0
        for ch in s:
            if ch == "(":
                cmin += 1
                cmax += 1
            elif ch == ")":
                cmax -= 1
                cmin = max(cmin - 1, 0)
            else:
                cmax += 1
                cmin = max(cmin - 1, 0)
            
            if cmax < 0:
                return False
        
        return cmin == 0