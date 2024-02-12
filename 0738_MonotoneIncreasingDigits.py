# 1st solution
# O(d) time | O(d) space
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(map(int, list(str(n))))
        if len(digits) == 1:
            return n
        
        def dfs(idx, front, limit):
            if idx == len(digits):
                return 0
            if limit:
                if digits[idx] < front:
                    return -1
                ans = -1
                for val in reversed(range(front, digits[idx] + 1)):
                    num = dfs(idx + 1, val, val >= digits[idx])
                    cand = num + val * pow(10, len(digits) - idx - 1)
                    if num >= 0:
                        if cand > ans:
                            ans = cand
                        else:
                            break
                return ans
            else:
                return pow(10, len(digits) - idx) - 1

    
        return dfs(0, 0, True)

# 2nd solution
# O(d) time | O(d) space
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        ones = 111111111
        result = 0
        for _ in range(9):
            while result + ones > n:
                ones //= 10
            result += ones
        return result