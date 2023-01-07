# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        low, high = 0, citations[-1]
        h = low
        while low < high:
            mid = low + (high - low) // 2
            idx = bisect.bisect_right(citations, mid)
            h = n - idx
            if h > mid:
                low = mid + 1
            else:
                high = mid
        return low