# 1st solution
# O(n) time| O(1) space
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        table = {}
        for i in range(len(time)):
            remainder = time[i] % 60
            table[remainder] = table.get(remainder, 0) + 1
        count = 0
        for i in range(1, 30):
            count += table.get(i, 0) * table.get(60 - i, 0)
        for i in [0, 30]:
            n = table.get(i, 0)
            count += n * (n - 1) // 2
        # print(table)
        return count
