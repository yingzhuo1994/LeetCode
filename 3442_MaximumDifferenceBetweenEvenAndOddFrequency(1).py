# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        odd = 0
        even = len(s)
        for freq in cnt.values():
            if freq & 1:
                odd = max(odd, freq)
            else:
                even = min(even, freq)
        return odd - even