# 1st solution, TLE
# # O(n^2) time | O(n) space
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0
        bulbs = [True for _ in range(n)]
        for start in range(2, n):
            for i in range(start - 1, n, start):
                bulbs[i] = not bulbs[i]
            # print(start, bulbs)
        if n > 1:
            bulbs[-1] = not bulbs[-1]
        return sum(bulbs)

# 2nd solution
# # O(n) time | O(1) space
class Solution:
    def bulbSwitch(self, n: int) -> int:
        i = 1
        count = 0
        d = 3
        while i < n:
            count += 1
            i += d
            d += 2
        if i != n:
            count += 1
        return count