class Solution:
    # 1st solution
    # O(n) time | O(1) space
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            curSum = numbers[left] + numbers[right]
            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:
                return [left + 1, right + 1]