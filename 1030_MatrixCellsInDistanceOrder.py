# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cal_distance = lambda A: (abs(A[0] - rCenter) + abs(A[1] - cCenter))
        lst = []
        for i in range(rows):
            for j in range(cols):
                lst.append([i, j])
        lst.sort(key = lambda A: cal_distance(A))
        return lst