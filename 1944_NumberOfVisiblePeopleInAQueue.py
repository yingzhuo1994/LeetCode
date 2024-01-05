# 1st solution
# O(n) time | O(n) space
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0 for _ in range(n)]
        stack = [heights[-1]]
        for i in reversed(range(n - 1)):
            count = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            if stack:
                count += 1
            stack.append(heights[i])
            ans[i] = count
        return ans