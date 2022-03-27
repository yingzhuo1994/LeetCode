# 1st solution
# O(m * n + m*log(m)) time | O(m) length
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        array = [[sum(row), i] for i, row in enumerate(mat)]
        array.sort()
        return [array[i][1] for i in range(k)]