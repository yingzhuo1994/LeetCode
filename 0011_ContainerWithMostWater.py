# 1st brute-force solution
# O(n^2) time | O(1) space 
class Solution:
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
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left, right = 0, len(height) - 1
        while left < right:
            w = right - left
            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1
            curArea = w * h
            area = max(area, curArea)
        return area
