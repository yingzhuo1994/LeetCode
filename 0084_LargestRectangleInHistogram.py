class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0
        for i in range(len(heights)):
            current_area = self.get_area(heights, i)
            if current_area > largest_area:
                largest_area = current_area
        return largest_area
    
    def get_area(heights, i):
        left = i
        right = i
        while left > 0:
            if heights[left] <= heights[i]:
                left -= 1
    