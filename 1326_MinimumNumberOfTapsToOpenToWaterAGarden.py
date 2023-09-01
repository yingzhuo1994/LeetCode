# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        intervals = [[max(i - ranges[i], 0), min(i + ranges[i], n)] for i in range(n + 1) if ranges[i] > 0]
        intervals.sort()
        print(intervals)

        left, right = 0, 0
        count = 1
        for a, b in intervals:
            if b <= right:
                continue
            elif a <= left:
                right = b
            elif a <= right:
                left, right = right, b
                count += 1
            else:
                return -1
        
        if right < n:
            return -1
        return count

# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [0] + [n + 2] * n
        for i, x in enumerate(ranges):
            for j in range(max(i - x + 1, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - x)] + 1)

        return dp[n] if dp[n] < n + 2 else -1

# 3rd solution
# O(n) time | O(n) space
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = [0] * (n + 1)
        
        for i, r in enumerate(ranges):
            left, right = max(0, i - r), min(n, i + r)
            max_range[left] = max(max_range[left], right - left)
        
		# it's a jump game now
        start = end = step = 0
        
        while end < n:
            step += 1
            start, end = end, max(i + max_range[i] for i in range(start, end + 1))
            if start == end:
                return -1
            
        return step