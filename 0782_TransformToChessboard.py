# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        if n <= 1:
            return 0
        rows=[''.join(str(c) for c in r) for r in board]
        counter = collections.Counter(rows)
        keys = list(counter)
        if len(keys) != 2 or abs(counter[keys[0]] - counter[keys[1]]) > 1 \
            or abs(keys[0].count('1') - keys[0].count('0')) > 1 \
            or any(a == b for a, b in zip(*keys)):
            return -1
        rowdiff = sum(board[0][i] != (i % 2) for i in range(n))
        coldiff = sum(board[i][0] != (i % 2) for i in range(n))
        rowdiff = n - rowdiff if rowdiff %2 != 0 or (n % 2 == 0 and (n - rowdiff) < rowdiff) else rowdiff
        coldiff = n - coldiff if coldiff %2 != 0 or (n % 2 == 0 and (n - coldiff) < coldiff) else coldiff
        return (rowdiff + coldiff) // 2

# 2nd solution
# O(n^2) time | O(n^2) space
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        if len(board) <= 1:
            return 0
        
        rows = []
        for i in range(len(board)):
            rows.append(''.join(str(c) for c in board[i]))
        
        uniq_rows_cnt = collections.Counter(rows)
        uniq_rows = list(uniq_rows_cnt.keys())
        if len(uniq_rows) != 2:
            return -1
        if abs(uniq_rows_cnt[uniq_rows[0]] - uniq_rows_cnt[uniq_rows[1]]) > 1:
            return -1
        if abs(uniq_rows[0].count('0') - uniq_rows[0].count('1')) > 1:
            return -1
        
        # for two different rows, the values in the same column cannot be the same
        for i in range(len(uniq_rows[0])):
            if uniq_rows[0][i] == uniq_rows[1][i]:
                return -1
        
        n = len(board)
        
        # Given the first row, how many bits does it differ from the expected
        # row cells if we assume the row starts with 0 and alternates, e.g: 010101...
        row_diff = 0
        for j in range(n):
            if board[0][j] != j % 2:
                row_diff += 1
        if n % 2 == 0:
            row_diff = min(row_diff, n - row_diff)
        elif row_diff % 2 != 0:
            row_diff = n - row_diff

        
        # Similarly given the first column, how does it differ if we expect the column
        # starts with 0 and alternates
        col_diff = 0
        for i in range(n):
            col_diff += board[i][0] != i % 2
        if n % 2 == 0:
            col_diff = min(col_diff, n - col_diff)
        elif col_diff % 2 != 0:
            # first cell has to be 1
            col_diff = n - col_diff
        
        return (row_diff + col_diff) // 2
