# 1st solution
# O(n) time | O(n) space
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                lastIdx = stack.pop()
                result[lastIdx] = i - lastIdx
            stack.append(i)
        return result
