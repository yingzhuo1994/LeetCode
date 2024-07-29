# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for i, val in enumerate(rating):
            left = [rating[j] for j in range(i) if rating[j] < val]
            right = [rating[j] for j in range(i + 1, len(rating)) if rating[j] > val]
            ans += len(left) * len(right)

            left = [rating[j] for j in range(i) if rating[j] > val]
            right = [rating[j] for j in range(i + 1, len(rating)) if rating[j] < val]
            ans += len(left) * len(right)
        return ans


# 2nd solution
# O(n^2) time | O(1) space
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        n = len(rating)
        for i in range(1, n - 1):
            val = rating[i]
            left_low = 0
            left_high = 0
            for j in range(i):
                if rating[j] < val:
                    left_low += 1
                elif rating[j] > val:
                    left_high += 1

            right_low = 0
            right_high = 0
            for j in range(i + 1, n):
                if rating[j] < val:
                    right_low += 1
                elif rating[j] > val:
                    right_high += 1
            ans += left_low * right_high + left_high * right_low

        return ans