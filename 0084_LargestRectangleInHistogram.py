class Solution:
    # 1st solution
    # O(n^2) time | O(1) space
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0
        for i in range(len(heights)):
            current_area = self.get_area(heights, i)
            print(i, current_area)
            if current_area > largest_area:
                largest_area = current_area
        return largest_area
    
    def get_area(self, heights, i):
        left = i
        right = i
        while left >= 0 and heights[left] >= heights[i]:
            left -= 1
        while right < len(heights) and heights[right] >= heights[i]:
            right += 1
        return (right - left - 1) * heights[i]

    # 2nd solution
    # O(n) time | O(1) space
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans
