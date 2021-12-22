# 1st solution
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



        
