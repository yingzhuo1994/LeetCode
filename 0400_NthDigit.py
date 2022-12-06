# 1st solution
# O(log(n)) time | O(1) space
class Solution:
    def findNthDigit(self, n: int) -> int:
        k = 0
        curSum = 0
        while curSum < n:
            k += 1
            curSum += 9 * k * 10**(k-1)
        curSum -= 9 * k * 10**(k-1)
        n -= curSum
        a = (n -1) // k
        b = (n -1) % k
        num = 10**(k-1) + a
        s = str(num)
        return int(s[b])