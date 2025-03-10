# 1st solution
# O(n) time | O(1) space
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        ans = 0
        for i in range(len(s) - k + 1):
            val = int(s[i:i+k])
            if val and num % val == 0:
                ans += 1
        return ans