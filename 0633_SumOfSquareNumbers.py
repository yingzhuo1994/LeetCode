# 1st solution
# O(sqrt(c)) time | O(sqrt(c)) space
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        lst = []
        num = 0
        while num * num <= c:
            lst.append(num * num)
            num += 1
        
        left, right = 0, len(lst) - 1
        while left <= right:
            curSum = lst[left] + lst[right]
            if curSum > c:
                right -= 1
            elif curSum < c:
                left += 1
            else:
                return True
        return False