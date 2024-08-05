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

# 2nd solution
# O(log(n)) time | O(log(n)) space
# n = log(num)
class Solution:
    def findIntegers(self, n):
        s = bin(n + 1)[2:]
        k = len(s)
        dp = [1, 2] + [0]*(k-2)
        for i in range(2, k):
            dp[i] = dp[i-1] + dp[i-2]

        flag, ans = 0, 0
        for i in range(k):
            if s[i] == "0":
                continue
            if flag == 1:
                break
            if i > 0 and s[i-1] == "1":
                flag = 1
            ans += dp[k-1-i]
        
        return ans

# 3rd solution
# O(log(n)) time | O(1) space
# n = log(num)
class Solution:
    def findIntegers(self, n):
        x, y = 1, 2
        res = 0
        n += 1
        while n:
            if n & 1 and n & 2:
                res = 0
            res += x * (n & 1)
            n >>= 1
            x, y = y, x + y
        return res
    
# 4th solution
# O(log(n)) time | O(log(n)) space
# n = log(num)
class Solution:
    def findIntegers(self, n: int) -> int:
        @cache
        def dfs(i: int, pre1: bool, is_limit: bool) -> int:
            if i < 0:
                return 1
            up = n >> i & 1 if is_limit else 1
            res = dfs(i - 1, False, is_limit and up == 0)  # 填 0
            if not pre1 and up == 1:  # 可以填 1
                res += dfs(i - 1, True, is_limit)  # 填 1
            return res
        return dfs(n.bit_length() - 1, False, True)  # 从高位到低位