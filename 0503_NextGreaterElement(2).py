# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        for i, num in enumerate(nums):
            isFound = False
            for j in range(i + 1, n):
                if nums[j] > num:
                    ans[i] = nums[j]
                    isFound = True
                    break
            if isFound:
                continue
            for j in range(i):
                if nums[j] > num:
                    ans[i] = nums[j]
                    break
        return ans

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        idx = 0
        maxNum = nums[0]
        n = len(nums)
        for i in range(n):
            if nums[i] >= maxNum:
                idx = i
                maxNum = nums[i]
        index = [None] * n
        for i in reversed(range(idx)):
            if nums[i] == maxNum:
                continue
            j = i + 1
            while j is not None:
                if nums[j] > nums[i]:
                    index[i] = j
                    break
                else:
                    j = index[j]
        
        for i in reversed(range(idx + 1, n)):
            if nums[i] == maxNum:
                continue

            j = i + 1
            while j is not None:
                if nums[j%n] > nums[i]:
                    index[i] = j % n
                    break
                else:
                    j = index[j%n]
        
        ans = [-1] * n

        for i in range(n):
            ans[i] = nums[index[i]] if index[i] is not None else -1
        return ans