# 1st solution
# O(n!) time | O(n) space
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visitedCols = set()
        visitedDigs = set()
        visitedAnti = set()
        ans = []
        def helper(x, y, lst):
            if len(lst) == n:
                if not ans or ans[-1] != lst:
                    ans.append(lst)
                return
            if y in visitedCols or x - y in visitedDigs or x + y in visitedAnti:
                return

            visitedCols.add(y)
            visitedDigs.add(x - y)
            visitedAnti.add(x + y)
            cur = ""
            for k in range(n):
                if k == y:
                    cur += "Q"
                else:
                    cur += "."
            for j in range(n):
                helper(x + 1, j, lst + [cur])
            visitedCols.remove(y)
            visitedDigs.remove(x - y)
            visitedAnti.remove(x + y)

        for j in range(n):
            helper(0, j, [])

        return ans
                    
                    