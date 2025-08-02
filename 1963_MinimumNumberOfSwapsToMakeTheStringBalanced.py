# 1st solution
# O(n) time | O(1) space
class Solution:
    def minSwaps(self, s: str) -> int:
        left = 0
        right = 0
        for ch in s:
            if ch == "[":
                left += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    right += 1
        k = (left + right) // 2
        q, r = divmod(k, 2)
        return q + r