# 1st solution
# O(n) time | O(1) space
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        zero = 0
        one = 0
        start = 0
        ans = 0
        for i, ch in enumerate(s):
            if ch == "0":
                zero += 1
            else:
                one += 1
            while min(one, zero) > k:
                if s[start] == "0":
                    zero -= 1
                else:
                    one -= 1
                start += 1
            ans += i - start + 1
        return ans