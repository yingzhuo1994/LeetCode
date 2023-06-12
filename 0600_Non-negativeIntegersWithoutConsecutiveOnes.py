# 1st solution, TLE
class Solution:
    def findIntegers(self, n: int) -> int:
        ans = 2
        level = set([0, 1])
        d = 1
        while level:
            newLevel = set()
            for num in level:
                s = str(bin(num))
                for i in range(2, len(s)):
                    num1 = s[:i+1] + "0" + s[i+1:]
                    num1 = int(num1, 2)
                    if (1 << d) <= num1 <= n:
                        newLevel.add(num1)
                    if s[i] != "1" and (i + 1 >= len(s) or s[i+1] != "1"):
                        num2 = s[:i+1] + "1" + s[i+1:]
                        num2 = int(num2, 2)
                        if (1 << d) <= num2 <= n:
                            newLevel.add(num2)
            d += 1
            ans += len(newLevel)
            level = newLevel
        
        return ans
