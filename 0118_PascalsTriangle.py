class Solution:
    # 1st Recursive Solution
    # def generate(self, numRows: int) -> List[List[int]]:
    #     def helper(n):
    #         if n == 1:
    #             return [1]
    #         else:
    #             lst = [1 for _ in range(n)]
    #             lastRow = helper(n - 1)
    #             for i in range(1, n - 1):
    #                 lst[i] = lastRow[i - 1] + lastRow[i]
    #             return lst
    #     lst = [helper(r) for r in range(1, numRows + 1)]
    #     return lst

    # 2nd Iterative Solution
    # def generate(self, numRows: int) -> List[List[int]]:
    #     lst = [[1]]
    #     for i in range(2, numRows + 1):
    #         curRow = [1 for _ in range(i)]
    #         lastRow = lst[i-2]
    #         for j in range(1, i - 1):
    #             curRow[j] = lastRow[j - 1] + lastRow[j]
    #         lst.append(curRow)
    #     return lst

    # 3rd Solution
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res
