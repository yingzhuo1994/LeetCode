class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {-1: 0, 0: 1}
        k = 1
        while k <= n:
            oneStep = dic[k - 1]
            twoStep = dic[k - 2]
            total = oneStep + twoStep
            dic[k] = total
            k += 1
        return dic[n]
