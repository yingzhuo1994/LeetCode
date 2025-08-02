# 1st solution
# O(n) time | O(n) space
from bisect import bisect
from itertools import accumulate
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefixSum = list(accumulate(chalk))
        r = k % prefixSum[-1]
        idx = bisect.bisect_right(prefixSum, r)
        return idx
