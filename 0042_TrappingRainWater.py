# 1st solution, brute force
# O(n^2) time | O(1) space
class Solution:
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
class Solution:
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
    
# 3rd solution, using stacks
# O(n) time | O(n) space
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        current = 0
        stack = []
        while current < len(height):
            while stack and height[current] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                ans += distance * bounded_height
            stack.append(current)
            current += 1
        return ans

# 4th solution, using two pointers
# O(n) time | O(1) space
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        left_max = 0
        right_max = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1  
        return ans