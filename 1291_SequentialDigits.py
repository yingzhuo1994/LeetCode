# 1st solution
# O(1) time | O(1) space
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for length in range(len(str(low)), len(str(high)) + 1):
            for d in range(1, 10):
                if d + length - 1 > 9:
                    break
                num = 0
                for k in reversed(range(length)):
                    num += (d + length - 1 - k) * 10**k
                if num < low or num > high:
                    continue
                ans.append(num)
        return ans
