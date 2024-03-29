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
    
# 2nd solution
# O(n) time | O(1) space
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        def countSubarray(array, start, end):
            if not array:
                return 0
            count = 0
            minIdx = -1
            maxIdx = -1
            for i in range(start, end):
                num = nums[i]
                if num == minK:
                    minIdx = max(minIdx, i)
                if num == maxK:
                    maxIdx = max(maxIdx, i)
                if minIdx >= 0 and maxIdx >= 0:
                    frontIdx = min(minIdx, maxIdx)
                    count += frontIdx - start + 1
            return count

        n = len(nums)
        start = 0
        ans = 0
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                ans += countSubarray(nums, start, i)
                start = i + 1

        if nums[n-1] >= minK and nums[n-1] <= maxK:
            ans += countSubarray(nums, start, n)
        
        return ans

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        minIdx = -1
        maxIdx = -1
        start = -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                start = i
            else:
                if num == minK:
                    minIdx = i
                if num == maxK:
                    maxIdx = i
                ans += max(0, min(minIdx, maxIdx) - start)
        return ans