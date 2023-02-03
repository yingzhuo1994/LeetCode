# 1st solution
# O(n) time | O(n) space
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        stack = []
        k = numRows
        for i in range(0, len(s), 2 * k - 2):
            stack.append(s[i])
        for i in range(1, k - 1):
            for a in range(i, len(s), 2 * k - 2):
                stack.append(s[a])
                b = a + 2 * (k - 1 - a % (2 * k - 2))
                if b < len(s):
                    stack.append(s[b])
        for i in range(k - 1, len(s), 2 * k - 2):
            stack.append(s[i])
        return "".join(stack)

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        stack = [[] for _ in range(numRows)]
        i = 0
        while i < len(s):
            for row in range(numRows):
                if i >= len(s):
                    break
                stack[row].append(s[i])
                i += 1
            for row in reversed(range(1, numRows-1)):
                if i >= len(s):
                    break
                stack[row].append(s[i])
                i += 1
        ans = []
        for row in range(numRows):
            ans.extend(stack[row])
        return "".join(ans)

# 3rd solution
# O(n) time | O(n) space
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if n <= numRows or numRows == 1:
            return s
        stack =[[] for _ in range(numRows)]
        j = 0
        d = 1
        for ch in s:
            stack[j].append(ch)
            j += d
            if j == numRows:
                j = numRows - 2
                d = - 1
            elif j == -1:
                j = 1
                d = 1
        ans = ["".join(line) for line in stack]
        return "".join(ans)