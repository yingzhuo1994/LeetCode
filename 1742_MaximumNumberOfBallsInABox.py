# 1st solution
# O(n) time | O(n) space
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        cnt = Counter()
        for num in range(lowLimit, highLimit + 1):
            key = 0
            while num > 0:
                key += num % 10
                num //= 10
            cnt[key] += 1
        return max(cnt.values())