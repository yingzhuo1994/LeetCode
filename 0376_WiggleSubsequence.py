# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]

        ans = 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                elif nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
            ans = max(ans, max(dp[i]))
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        largerState = [1, nums[0]]
        smallerState = [1, nums[0]]

        for i in range(1, n):
            newLargerState = largerState[:]
            newSmallerState = smallerState[:]

            if nums[i] > smallerState[1]:
                length = smallerState[0] + 1
                if length > largerState[0] or (length == largerState[0] and nums[i] > largerState[1]):
                    newLargerState = [length, nums[i]]
            
            if nums[i] < largerState[1]:
                length = largerState[0] + 1
                if length > smallerState[0] or (length == smallerState[0] and nums[i] < smallerState[1]):
                    newSmallerState = [length, nums[i]]
            
            largerState = newLargerState
            smallerState = newSmallerState
        
        ans = max(largerState[0], smallerState[0])
        return ans

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        down, up = 1, 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        
        return max(up, down)

# 4th solution, Greedy Approach
# O(n) time | O(1) space
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        prevDiff = nums[1] - nums[0]
        count = 2 if prevDiff != 0 else 1

        for i in range(2, n):
            diff = nums[i] - nums[i-1]
            if (diff > 0 and prevDiff <= 0) or (diff < 0 and prevDiff >= 0):
                count += 1
                prevDiff = diff
        
        return count