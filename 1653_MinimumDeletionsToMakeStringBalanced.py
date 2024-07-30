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

# 2nd
# O(n) time | O(n) space
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        dp_a = [0 for _ in range(n + 1)]
        dp_b = [0 for _ in range(n + 1)]
        for i, ch in enumerate(s):
            dp_a[i] = dp_a[i - 1]
            dp_b[i] = dp_b[i - 1]
            if ch == "a":
                dp_a[i] += 1
            else:
                dp_b[i] += 1
        ans = float("inf")
        for i in range(n + 1):
            count = dp_b[i - 1] + dp_a[n-1] - dp_a[i - 1]
            ans = min(ans, count)
        return ans

# 2nd
# O(n) time | O(1) space
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_total = s.count("a")
        a_count = 0
        ans = float("inf")
        for i in range(n + 1):
            if i > 0 and s[i - 1] == "a":
                a_count += 1
            count = i - a_count + a_total - a_count
            ans = min(ans, count)
        return ans