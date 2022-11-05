# 1st solution
# o(n^2) time | O(n^2) space
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        def is_close(a, b):
            if a == "z":
                return b == "a"
            return ord(b) - ord(a) == 1
        
        def dfs(start, end, memo):
            if start > end:
                return
            a, b = p[start], p[end]
            length = end - start + 1
            if (a, b, length) in memo:
                return

            memo.add((a, b, length))
            dfs(start + 1, end, memo)
            dfs(start, end - 1, memo)

        memo = set()
        start = 0
        end = 0
        for i in range(len(p)):
            if i > 0:
                if is_close(p[i-1], p[i]):
                    end = i
                else:
                    start = i
                    end = i
            dfs(start, end, memo)
        return len(memo)