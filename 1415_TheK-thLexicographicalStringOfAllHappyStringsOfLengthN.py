# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        lst = []
        def dfs(s):
            if len(s) == n:
                lst.append(s)
                return
            for ch in "abc":
                if not s or s[-1] != ch:
                    dfs(s + ch)
        dfs("")
        lst.sort()
        if k <= len(lst):
            return lst[k - 1]
        return ""