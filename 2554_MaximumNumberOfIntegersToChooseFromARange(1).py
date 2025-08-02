# 1st solution
# O(n + k * log(k)) time | O(k) space
# where k = len(banned)
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        ans = 0
        curSum = 0
        i = 0
        for num in range(1, n + 1):
            while i < len(banned) and num > banned[i]:
                i += 1
            if i < len(banned) and num == banned[i]:
                continue
            else:
                curSum += num
                if curSum <= maxSum:
                    ans += 1
                else:
                    break
        return ans