# 1st solution
# O(n * log(M)) time | O(1) space
# where n = len(candies) and M = max(candies)
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def enough(target):
            if k * target > total:
                return False
            num = 0
            for candy in candies:
                num += candy // target
                if num >= k:
                    return True
            return False
        total = sum(candies)
        if total < k:
            return 0
        start = 1
        end = max(candies)
        ans = 0
        while start <= end:
            mid = start + (end - start) // 2
            if enough(mid):
                ans = max(ans, mid)
                start = mid + 1
            else:
                end = mid - 1
        return ans