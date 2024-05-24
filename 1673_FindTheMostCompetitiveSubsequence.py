# 1st solution
# O(n) time | O(k) space
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)
        for i in range(n):
            while len(stack) > max(k - (n - i), 0) and stack[-1] > nums[i]:
                stack.pop()
            stack.append(nums[i])

        while len(stack) > k:
            stack.pop()
        return stack