# O(1) time | O(1) space
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Each iteration does one thing
        # There is no difference in time complexity, and space complexity.
        # As a software engineer, you should write clean code which is easy to understand.
        rowDic = [set() for _ in range(9)]
        columnDic = [set() for _ in range(9)]
        boxDic = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if board[i][j] == '.':
                    continue
                # check row
                if elem in rowDic[i]:
                    return False
                else:
                    rowDic[i].add(elem)

        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if board[i][j] == '.':
                    continue
        
                # check column
                if elem in columnDic[j]:
                    return False
                else:
                    columnDic[j].add(elem)

        for i in range(9):
            for j in range(9):
                elem = board[i][j]
                if board[i][j] == '.':
                    continue

                # check sub-box
                x, y = i // 3, j // 3
                if elem in boxDic[3*x+y]:
                    return False
                else:
                    boxDic[3*x+y].add(elem)
        return True
