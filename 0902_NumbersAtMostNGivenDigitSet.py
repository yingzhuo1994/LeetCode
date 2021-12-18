class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        if n == 0:
            return 0

        length = 0
        while 10**length <= n:
            length += 1
        
        k = len(digits)
        
        if k != 1:
            rest = k * (1 - k**(length - 1)) // (1 - k)
        else:
            rest = length - 1

        digitSet = set([int(digit) for digit in digits])

        front = self.fullDigit(digitSet, n, k, length)
        
        return front + rest

    def fullDigit(self, digitSet, n, k, length):
        if length == 1:
            count = 0
            for i in range(1, n + 1):
                if i in digitSet:
                    count += 1
            return count
        count = 0
        firstDigit = n // 10**(length - 1)
        for i in range(1, firstDigit):
            if i in digitSet:
                count += 1

        if firstDigit in digitSet:
            return self.fullDigit(digitSet, n % 10**(length - 1), k, length - 1) + count * k**(length - 1)
        else:
            return count * k**(length - 1)

# 2nd solution
#  O(log(n)) time | O(log(n)) space
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        S = str(n)
        K = len(S)
        dp = [0] * K + [1]
        # dp[i] = total number of valid integers if n was "n[i:]"

        for i in reversed(range(K)):
            # Compute dp[i]

            for d in digits:
                if d < S[i]:
                    dp[i] += len(digits) ** (K-i-1)
                elif d == S[i]:
                    dp[i] += dp[i+1]

        return dp[0] + sum(len(digits) ** i for i in range(1, K))



        
