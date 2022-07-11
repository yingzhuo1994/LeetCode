# 1st solution
# O(n) time | O(n) space
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in reversed(range(n-1)):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def candy(self, ratings: List[int]) -> int:
        def count(k):
            return (k * (k + 1)) // 2
        
        n = len(ratings)
        if n <= 1:
            return n
        
        candies = 0
        up, down = 0, 0
        oldSlope = 0

        for i in range(1, n):
            newSlope = ratings[i] - ratings[i - 1]

            if (oldSlope > 0 and newSlope == 0) or (oldSlope < 0 and newSlope >= 0):
                candies += count(up) + count(down) + max(up, down)
                up = 0
                down = 0

            if newSlope > 0:
                up += 1
            elif newSlope < 0:
                down += 1
            else:
                candies += 1

            oldSlope = newSlope

        candies += count(up) + count(down) + max(up, down) + 1
        return candies