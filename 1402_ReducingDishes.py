# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        negPart = []
        nonNegPart = []
        for num in satisfaction:
            if num < 0:
                negPart.append(num)
            else:
                nonNegPart.append(num)
        if len(nonNegPart) == 0:
            return 0
        negPart.sort(reverse=True)
        nonNegPart.sort()

        extraSum = sum(nonNegPart)
        curSum = sum([i * num for i, num in enumerate(nonNegPart, 1)])

        for i in range(len(negPart)):
            extraSum += negPart[i]
            if extraSum > 0:
                curSum += extraSum
            else:
                break
        return curSum
