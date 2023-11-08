# 1st solution
# O(n) time | O(1) space
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        zero = 0
        one = 0
        for ch in s:
            if ch == "0":
                if one > 0:
                    zero = 1
                    one = 0
                else:
                    zero += 1
            else:
                one += 1
                ans = max(ans, min(one, zero))
        return ans * 2