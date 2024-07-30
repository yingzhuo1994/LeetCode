# 1st solution, TLE
# O(2^n) time | O(n) space
class Solution:
    def minimumDeletions(self, s: str) -> int:
        self.ans = float("inf")

        def dfs(idx, cur, count):
            if count >= self.ans:
                return
            if idx == len(s):
                self.ans = min(self.ans, count)
                return
            if s[idx] == cur:
                dfs(idx + 1, cur, count)
            else:
                if cur == "a":
                    dfs(idx + 1, "a", count + 1)
                    dfs(idx + 1, "b", count)
                else:
                    dfs(idx + 1, "b", count + 1)
        dfs(0, "a", 0)
        return self.ans