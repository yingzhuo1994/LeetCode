# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxScore(self, s: str) -> int:
        zeros = s.count("0")
        ones = len(s) - zeros

        zero, one = 0, ones
        if s[0] == "0":
            zero += 1
        else:
            one -= 1
        ans = zero + one
        for i in range(1, len(s) - 1):
            if s[i] == "0":
                zero += 1
            else:
                one -= 1
            ans = max(ans, zero + one)
        return ans