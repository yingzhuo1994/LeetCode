# O(log(maxSum)) time | O(1) space
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            total = mid + self.getSideSum(mid - 1, index) + self.getSideSum(mid - 1, n - index - 1)
            if total <= maxSum:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
    

    def getSideSum(self, value, number):
        if number > value:
            return (1 + value) * value // 2 + (number - value)
        else:
            return (value + value - number + 1) * number // 2