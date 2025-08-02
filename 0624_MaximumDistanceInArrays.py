# 1st solution
# O(m) time | O(1) space
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        minVal1 = [float("inf"), -1]
        minVal2 = [float("inf"), -1]
        maxVal1 = [float("-inf"), -1]
        maxVal2 = [float("-inf"), -1]
        for i in range(m):
            array = arrays[i]
            if array[0] < minVal1[0]:
                minVal1, minVal2 = [array[0], i], minVal1
            elif array[0] < minVal2[0]:
                minVal2 = [array[0], i]
            if array[-1] > maxVal1[0]:
                maxVal1, maxVal2 = [array[-1], i], maxVal1
            elif array[-1] > maxVal2[0]:
                maxVal2 = [array[-1], i]
        if minVal1[1] != maxVal1[1]:
            return maxVal1[0] - minVal1[0]
        return max(abs(maxVal2[0] - minVal1[0]), abs(maxVal1[0] - minVal2[0]))