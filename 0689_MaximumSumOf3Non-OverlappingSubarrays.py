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



