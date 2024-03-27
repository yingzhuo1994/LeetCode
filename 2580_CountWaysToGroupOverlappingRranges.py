# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        ranges.sort()
        last = -1
        count = 0
        for start, end in ranges:
            if start > last:
                count += 1

            last = max(last, end)
        
        return pow(2, count) % MOD
