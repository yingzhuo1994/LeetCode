# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

# 1st solution
# O(n) time | O(1) space
class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)
            if res > 0:
                low = mid + 1
            elif res < 0:
                high = mid - 1
            else:
                return mid
        return -1