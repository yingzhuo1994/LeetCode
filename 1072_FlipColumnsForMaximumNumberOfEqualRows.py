# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        ans = 0
        memo = {}
        for row in matrix:
            key = "".join(map(str, row))
            memo[key] = memo.get(key, 0) + 1
        for key in memo:
            mask = "".join(["1" if ch == "0" else "0" for ch in key])
            count = memo.get(mask, 0) + memo[key]
            ans = max(ans, count)
        return ans
