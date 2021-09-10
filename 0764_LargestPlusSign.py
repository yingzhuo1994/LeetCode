class Solution:
    # 1st solution, brute-force method, TLE
    # O(n^3) time | O(1) space
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        maxOrder = n // 2 + 1
        while maxOrder > 0:
            for i in range(n):
                for j in range(n):
                    if self.check(n, mines, maxOrder, i, j):
                        return maxOrder
            maxOrder -= 1
        return 0

    def check(self, n, mines, order, x, y):
        if self.checkIndex(n, x, y):
            left = x - order + 1
            right = x + order - 1
            top = y - order + 1
            bottom = y + order - 1
            if self.checkIndex(n, left, right) and self.checkIndex(n, top, bottom):
                for i in range(left, right + 1):
                    if [i, y] in mines:
                        return False
                for j in range(top, bottom + 1):
                    if [x, j] in mines:
                        return False
                return True
            else:
                return False
        else:
            return False
    

    def checkIndex(self, n, i, j):
        if i < 0 or i >= n or j < 0 or j >= n:
            return False
        return True