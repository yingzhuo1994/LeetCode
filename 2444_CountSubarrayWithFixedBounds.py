# 1st solution, TLE
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def countSubarray(array):
            if not array:
                return 0
            minIdxList = []
            maxIdxList = []
            for i, num in enumerate(array):
                if num == minK:
                    minIdxList.append(i)
                if num == maxK:
                    maxIdxList.append(i)
            if not minIdxList or not maxIdxList:
                return 0
            k = len(array)
            dp = [[0 for _ in range(k)] for _ in range(k)]
            for x in minIdxList:
                for y in maxIdxList:
                    a, b = min(x, y), max(x, y)
                    for i in range(a + 1):
                        for j in range(b, k):
                            dp[i][j] = 1
            count = 0
            for i in range(k):
                for j in range(k):
                    count += dp[i][j]
            return count

        n = len(nums)
        start = 0
        ans = 0
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                ans += countSubarray(nums[start:i])
                start = i + 1

        if nums[n-1] >= minK and nums[n-1] <= maxK:
            ans += countSubarray(nums[start:n])
        
        return ans
    
