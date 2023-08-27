# 1st solution, MLE
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        stack = [[n, 1]]
        ans = 1
        while stack:
            newStack = []
            for left, k in stack:
                if left == k:
                    return ans
                elif left > k:
                    newStack.append([left - k, k])
                    newStack.append([left, n - left])
            ans += 1
            stack = newStack
