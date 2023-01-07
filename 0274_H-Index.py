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

# 2nd solution, Count sort
# O(n) time | O(1) space
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)

        for c in citations:
            if c > n:
                count[n] += 1
            else:
                count[c] += 1
        
        total = 0
        for i in reversed(range(n + 1)):
            total += count[i]
            if total >= i:
                return i
        
        return 0