# 1st solution
# O(n) time | O(n) space
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        newCode = code + code
        curSum = 0
        if k > 0:
            curSum = sum(newCode[n:n+k])
            for i in reversed(range(n)):
                ans[i] = curSum
                curSum -= newCode[i+k]
                curSum += newCode[i]
        else:
            curSum = sum(newCode[k:])
            for i in range(n):
                ans[i] = curSum
                curSum -= newCode[i+k]
                curSum += newCode[i]
        return ans


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans

        curSum = 0
        if k > 0:
            curSum = sum(code[:k])
            for i in reversed(range(n)):
                ans[i] = curSum
                curSum -= code[(i+k)%n]
                curSum += code[i]
        else:
            curSum = sum(code[k:])
            for i in range(n):
                ans[i] = curSum
                curSum -= code[i+k]
                curSum += code[i]
        return ans


# 3rd solution
# O(n) time | O(1) space
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        res = []
        n = len(code)
        code += code
        if k > 0:
            l, r = 1, k
        else:
            l, r = n + k, n - 1
        w = sum(code[l:r+1])
        for i in range(n):
            res.append(w)
            w -= code[l]
            w += code[r + 1]
            l, r = l + 1, r + 1
        return res