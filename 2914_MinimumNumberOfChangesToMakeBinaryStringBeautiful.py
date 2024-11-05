# 1st solution
# O(n) time | O(1) space
class Solution:
    def minChanges(self, s: str) -> int:
        one = 0
        zero = 0
        ans = 0
        for ch in s:
            if ch == "0":
                zero += 1
            else:
                one += 1
            val = zero + one
            if val & 1:
                continue
            ans += min(zero, one)
            one = 0
            zero = 0
        return ans
