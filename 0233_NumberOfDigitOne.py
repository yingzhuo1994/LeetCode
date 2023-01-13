# 1st solution, bottom-up
# O(d) time | O(d) space
# d is the digit number of n
class Solution:
    def countDigitOne(self, n: int) -> int:
        memo = {0: 0}
        k = 1
        while k <= n:
            last = k // 10
            count = 10 * memo[last] + last
            memo[k] = count
            k *= 10
        
        ans = 0
        while n > 0:
            d = len(str(n)) - 1
            first = n // pow(10, d)
            second = n % pow(10, d)
            ans += first * memo[pow(10, d)] + (second + 1 if first == 1 else pow(10, d))
            n = second
        return ans

# 2nd solution, bottom-up
# O(d) time | O(d) space
# d is the digit number of n
class Solution:
    def countDigitOne(self, n: int) -> int:
        def countDigitX(x, n):
            if n < x:
                return 0
            result = 0
            # number of appearances for one cycle when x appears at position i
            i = 1
            while n >= i:
                # complete cycle, one more complete cycle if current digit > x
                cycle = n // (i * 10) + (1 if n // i % 10 > x else 0)
                result += cycle * i
                # incomplete cycle if current digit == x
                if n // i % 10 == x:
                    result += n % i + 1
                i *= 10
            return result
        return countDigitX(1, n)