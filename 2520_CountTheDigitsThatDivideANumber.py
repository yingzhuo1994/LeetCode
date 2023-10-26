class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        for ch in str(num):
            if num % int(ch) == 0:
                ans += 1
        return ans