# 1st solution
# O(n) time | O(1) space
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even = 1
        odd = 0
        ans = 0
        curSum = 0
        for num in arr:
            curSum += num
            if curSum & 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1
            ans %= MOD
        return ans 
