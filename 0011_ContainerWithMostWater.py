class Solution:
    # 1st brute-force solution
    # O(n^2) time | O(1) space 
    def maxArea(self, height: List[int]) -> int:
        area_largest = 0
        for left in range(len(height) - 1):
            for right in range(left + 1, len(height)):
                area = (right - left) * min(height[left], height[right])
                if area > area_largest:
                    area_largest = area
        return area_largest

    # 2nd solution
    # O(n) time | O(1) space
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
