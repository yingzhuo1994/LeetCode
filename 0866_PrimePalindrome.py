# 1st solution
# O(n) time | O(1) space
class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(x):
            if x < 2 or x % 2 == 0:
                return x == 2
            for i in range(3, int(x**0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True
        if 8 <= n <= 11:
            return 11
        for x in range(10 ** (len(str(n)) / 2), 10**5):
            y = int(str(x) + str(x)[-2::-1])
            if y >= n and isPrime(y):
                return y