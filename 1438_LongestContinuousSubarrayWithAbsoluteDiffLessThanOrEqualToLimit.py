# 1st solution
# O(n * log(n) * log(n)) time | O(n) space
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        start, end = 1, n
        while start <= end:
            length = start + (end - start) // 2
            isValid = False
            minStack = []
            maxStack = []
            for i in range(length - 1):
                heappush(minStack, [nums[i], i])
                heappush(maxStack, [-nums[i], i])
            for i in range(length - 1, n):
                heappush(minStack, [nums[i], i])
                heappush(maxStack, [-nums[i], i])
                while minStack and minStack[0][1] <= i - length:
                    heappop(minStack)
                while maxStack and maxStack[0][1] <= i - length:
                    heappop(maxStack)

                diff = -maxStack[0][0] - minStack[0][0]
                if diff <= limit:
                    isValid = True
                    break

            if isValid:
                start = length + 1
            else:
                end = length - 1
        return start - 1