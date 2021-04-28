class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(1) time | O(1) space
        rowDic = [{} for _ in range(9)]
        columnDic = [{} for _ in range(9)]
        boxDic = [[{}, {}, {}] for _ in range(3)]
        # for i in range(9):
        #     for j in range(9):
        #         elem = board[i][j]
        #         if board[i][j] == '.':
        #             continue
        #         # check row
        #         if elem in rowDic[i]:
        #             return False
        #         else:
        #             rowDic[i][elem] = 1
        #
        #         # check column
        #         if elem in columnDic[j]:
        #             return False
        #         else:
        #             columnDic[j][elem] = 1
        #
        #         # check sub-box
        #         x, y = i // 3, j // 3
        #         if elem in boxDic[x][y]:
        #             return False
        #         else:
        #             boxDic[x][y][elem] = 1
        # return True

        # Each iteration does one thing
        # There is no difference in time complexity, and space complexity.
        # As a software engineer, you should write clean code which is easy to understand.
        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if board[i][j] == '.':
                    continue
                # check row
                if elem in rowDic[i]:
                    return False
                else:
                    rowDic[i][elem] = 1

        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if board[i][j] == '.':
                    continue
        
                # check column
                if elem in columnDic[j]:
                    return False
                else:
                    columnDic[j][elem] = 1

        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if board[i][j] == '.':
                    continue

                # check sub-box
                x, y = i // 3, j // 3
                if elem in boxDic[x][y]:
                    return False
                else:
                    boxDic[x][y][elem] = 1
        return True
