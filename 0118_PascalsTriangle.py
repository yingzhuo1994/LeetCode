class Solution:
    # 1st Recursive Solution
    def generate(self, numRows: int) -> List[List[int]]:
        def helper(n):
            if n == 1:
                return [1]
            else:
                lst = [1 for _ in range(n)]
                lastRow = helper(n - 1)
                for i in range(1, n - 1):
                    lst[i] = lastRow[i - 1] + lastRow[i]
                return lst
        lst = [helper(r) for r in range(1, numRows + 1)]
        return lst
