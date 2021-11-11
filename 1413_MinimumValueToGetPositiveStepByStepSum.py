# 1st solution
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        while True:
            cur = startValue
            isTrue = True
            for num in nums:
                cur += num
                if cur < 1:
                    isTrue = False
                    break
            if isTrue:
                return startValue
            startValue += 1
            