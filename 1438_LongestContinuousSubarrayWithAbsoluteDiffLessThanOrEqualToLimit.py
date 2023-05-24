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

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        minStack = []
        maxStack = []
        start = 0
        ans = 0
        for i in range(n):
            heappush(minStack, [nums[i], i])
            heappush(maxStack, [-nums[i], i])

            while -maxStack[0][0] - minStack[0][0] > limit:
                start += 1
                while minStack and minStack[0][1] < start:
                    heappop(minStack)
                while maxStack and maxStack[0][1] < start:
                    heappop(maxStack)
            
            ans = max(ans, i - start + 1)
        return ans

# 3rd solution
# O(n) time | O(n) space
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxStack = collections.deque()
        minStack = collections.deque()
        i = 0
        for num in nums:
            while len(maxStack) and num > maxStack[-1]: 
                maxStack.pop()
            while len(minStack) and num < minStack[-1]: 
                minStack.pop()
            maxStack.append(num)
            minStack.append(num)
            if maxStack[0] - minStack[0] > limit:
                if maxStack[0] == nums[i]: 
                    maxStack.popleft()
                if minStack[0] == nums[i]: 
                    minStack.popleft()
                i += 1
        return len(nums) - i