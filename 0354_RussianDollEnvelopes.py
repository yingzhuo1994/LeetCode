# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        n = len(envelopes)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if self.isSmallerThan(envelopes[j], envelopes[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
    def isSmallerThan(self, front, back):
        return front[0] < back[0] and front[1] < back[1]

# 2nd solution
# O(nlog(n)) time | O(n) space
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: [x[0], -x[1]])    
        dp = []
        for _, height in envelopes:
            left = bisect.bisect_left(dp, height)
            if left == len(dp): 
                dp.append(height)
            else: 
                dp[left] = height
        return len(dp)