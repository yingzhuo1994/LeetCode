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
            totalWater += minHeight - height[i] if minHeight - height[i] > 0 else 0
        return totalWater

    # 2nd solution, dynamic programming
    # O(n) time | O(n) space
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans = 0
        size = len(height)
        left_max = [0 for _ in range(size)] 
        right_max = [0 for _ in range(size)]
        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(height[i], left_max[i - 1])
        
        right_max[size - 1] = height[size - 1]
        for i in reversed(range(size - 1)):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]

        return ans