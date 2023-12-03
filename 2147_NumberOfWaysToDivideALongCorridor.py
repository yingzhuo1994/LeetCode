# 1st solution
# O(n) time | O(1) space 
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = corridor.count("S")
        if seats == 0 or seats & 1:
            return 0
        MOD = 10**9 + 7
        ans = 1
        count = 0
        for idx in range(len(corridor)):
            if corridor[idx] == "S":
                start = idx - 1
                break
        
        for i in range(idx, len(corridor)):
            if corridor[i] == "S":
                if count == 0:
                    ans *= i - start
                    ans %= MOD
                count += 1
            if count == 2:
                count = 0
                start = i
        return ans