# 1st solution
# O(n) time | O(n) space
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        elif n == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            return str(nums[0]) + "/" + "(" + "/".join([str(nums[i]) for i in range(1, n)]) + ")"

# 2nd solution
class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        r = self.getMax(nums, 0, n - 1)
        return r.str
    
    def getMax(self, nums, start, end):
        r = Result()
        r.val = -1.0

        if start == end:
            r.str = str(nums[start]) + ""
            r.val = float(nums[start])
        elif start + 1 == end:
            r.str = str(nums[start]) + "/" + str(nums[end])
            r.val = nums[start] / nums[end]
        else:
            for i in range(start, end):
                r1 = self.getMax(nums, start, i)
                r2 = self.getMin(nums, i + 1, end)
                quo = r1. val / r2.val
                if quo > r.val:
                    r.str = r1.str + "/" + ("(" + r2.str + ")" if end - i >= 2 else r2.str)
                    r.val = quo
        return r

    def getMin(self, nums, start, end):
        r = Result()
        r.val = float("inf")

        if start == end:
            r.str = str(nums[start]) + ""
            r.val = float(nums[start])
        elif start + 1 == end:
            r.str = str(nums[start]) + "/" + str(nums[end])
            r.val = nums[start] / nums[end]
        else:
            for i in range(start, end):
                r1 = self.getMin(nums, start, i)
                r2 = self.getMax(nums, i + 1, end)
                quo = r1. val / r2.val
                if quo < r.val:
                    r.str = r1.str + "/" + ("(" + r2.str + ")" if end - i >= 2 else r2.str)
                    r.val = quo
        return r

class Result:
    def __init__(self):
        self.val = 0
        self.str = ""