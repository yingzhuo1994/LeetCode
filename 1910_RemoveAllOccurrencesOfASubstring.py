# 1st solution
# O(kn) time | O(n) space
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        k = len(part)
        for i, ch in enumerate(s):
            stack.append(ch)
            if len(stack) >= len(part) and "".join(stack[-k:]) == part:
                stack = stack[:-k]
        return "".join(stack)

# 2nd solution
# O(n + k) time | O(n + m) space
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m = len(part)
        pi1 = [0] * m   # part 的前缀数组
        # 更新 part 的前缀数组
        j = 0
        for i in range(1, m):
            while j > 0 and part[i] != part[j]:
                j = pi1[j-1]
            if part[i] == part[j]:
                j += 1
            pi1[i] = j
        
        res = []
        pi2 = [0]   # res 的前缀数组
        for ch in s:
            # 模拟从左至右匹配的过程
            res.append(ch)
            # 更新 res 的前缀数组
            j = pi2[-1]
            while j > 0 and ch != part[j]:
                j = pi1[j-1]
            if ch == part[j]:
                j += 1
            pi2.append(j)
            if j == m:
                # 如果匹配成功，那么删去对应后缀
                pi2[-m:] = []
                res[-m:] = []
        return "".join(res)