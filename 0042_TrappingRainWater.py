class Solution:
    # 1st solution, brute force
    # O(n^2) time | O(1) space
    def trap(self, height: List[int]) -> int:
        totalWater = 0
        for i in range(1, len(height) - 1):
            leftMax = 0
            for idx in range(i):
                leftMax = max(leftMax, height[idx])
            rightMax = 0
            for idx in range(i + 1, len(height)):
                rightMax = max(rightMax, height[idx])
            minHeight = min(leftMax, rightMax)
            totalWater += minHeight - height[i] if minHeight - height[i] < 0 else 0
        return totalWater