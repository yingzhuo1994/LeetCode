# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        array = [0 for _ in range(n - k + 1)]
        curSum = sum(nums[-k+1:])
        for i in reversed(range(n - k + 1)):
            curSum += nums[i]
            if i + k < n:
                curSum -= nums[i + k]
            array[i] = curSum
        
        m = len(array)
        leftArray = [[0, -1] for _ in range(m)]
        rightArray = [[0, -1] for _ in range(m)]

        for i in range(m - k):
            if array[i] > leftArray[i + k - 1][0]:
                leftArray[i + k] = [array[i], i]
            else:
                leftArray[i + k] = leftArray[i + k - 1]

        for i in reversed(range(k, m)):
            if array[i] >= rightArray[i - k + 1][0]:
                rightArray[i - k] = [array[i], i]
            else:
                rightArray[i - k] = rightArray[i - k + 1]

        ans = [-1, -1, -1]
        maxSum = 0
        for i in range(k, m - k + 1):
            curSum = leftArray[i][0] + array[i] + rightArray[i][0]
            if curSum > maxSum:
                maxSum = curSum
                ans = [leftArray[i][1], i, rightArray[i][1]]

        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        ans = []
        sum1, maxSum1, maxSum1Idx = 0, 0, 0
        sum2, maxSum12, maxSum12Idx = 0, 0, ()
        sum3, maxTotal = 0, 0
        for i in range(k * 2, len(nums)):
            sum1 += nums[i - k * 2]
            sum2 += nums[i - k]
            sum3 += nums[i]
            if i >= k * 3 - 1:
                if sum1 > maxSum1:
                    maxSum1 = sum1
                    maxSum1Idx = i - k * 3 + 1
                if maxSum1 + sum2 > maxSum12:
                    maxSum12 = maxSum1 + sum2
                    maxSum12Idx = (maxSum1Idx, i - k * 2 + 1)
                if maxSum12 + sum3 > maxTotal:
                    maxTotal = maxSum12 + sum3
                    ans = [*maxSum12Idx, i - k + 1]
                sum1 -= nums[i - k * 3 + 1]
                sum2 -= nums[i - k * 2 + 1]
                sum3 -= nums[i - k + 1]
        return ans