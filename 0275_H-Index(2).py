# 1st solution
# O(log(n)) time | O(log(n)) space
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = citations[-1]
        n = len(citations)
        while low < high:
            mid = low + (high - low) // 2
            idx = bisect.bisect_right(citations, mid)
            h = n - idx
            if h > mid:
                low = mid + 1
            elif h < mid:
                high = mid
            else:
                return h
        return low