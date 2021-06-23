class Solution:
    # 1st solution
    # O(nlogn) time | O(n) space
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst = []
        for line in matrix:
            lst.extend(line)
        lst.sort()
        return lst[k - 1]