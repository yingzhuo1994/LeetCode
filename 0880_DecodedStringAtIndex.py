# 1st solution
# O(n) time | O(n) space
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = [[], 0]
        for ch in s:
            if ch.isdigit():
                d = int(ch)
                stack = [stack, stack[1] * d]
            else:
                stack[0].append(ch)
                stack[1] += 1

            if stack[1] >= k:
                break

        def dfs(stack, k):
            last, n = stack
            left = 0
            m = None
            if len(last) > 1 and type(last[1]) is int:
                m = last[1]
            left = len(last) - 2
            if m is None:
                return last[k- 1]
            repeat = (n - left) // m
            r = k - repeat * m
            if r > 0:
                return last[1 + r]
            else:
                return dfs(last[:2], (k - 1) % m + 1)

        return dfs(stack, k)

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = 0
        for i, c in enumerate(s):
            n = n * int(c) if c.isdigit() else n + 1

            if k <= n:
                break
        
        for j in range(i, -1, -1):
            c = s[j]
            if c.isdigit():
                n //= int(c)
                k %= n
            else:
                if k == n or k == 0:
                    return c
                n -= 1