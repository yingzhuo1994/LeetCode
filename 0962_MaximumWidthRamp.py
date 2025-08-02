# 1st solution
# O(n * log(n)) time | O(1) space
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        start, end = 1, n - 1
        while start <= end:
            mid = start + (end - start) // 2
            enough = False
            minValue = nums[0]
            for i in range(mid, n):
                minValue = min(minValue, nums[i - mid])
                if nums[i] >= minValue:
                    enough = True
                    break

            if enough:
                ans = max(ans, mid)
                start = mid + 1
            else:
                end = mid - 1
        return ans

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        maxWidth = 0

        stack = []
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)

        for i in reversed(range(n)):
            while stack and nums[stack[-1]] <= nums[i]:
                pos = stack.pop()
                maxWidth = max(maxWidth, i - pos)
        return maxWidth