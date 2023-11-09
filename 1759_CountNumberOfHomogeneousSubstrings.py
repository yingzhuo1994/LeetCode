# 1st solution
# O(n) time | O(1) space
class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        ans = 0
        last = ""
        count = 0
        for i, ch in enumerate(s + "+"):
            if ch == last:
                count += 1
            else:
                ans += (count + 1) * count // 2
                ans %= MOD
                last = ch
                count = 1
        return ans