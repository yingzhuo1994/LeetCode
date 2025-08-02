# 1st solution
# O(1) time | O(1) space
class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(1, 3):
            for j in range(1, 3):
                count = 0
                for x, y in [[i - 1, j - 1], [i - 1, j], [i, j - 1], [i, j]]:
                    if grid[x][y]== "B":
                        count += 1
                if count != 2:
                    return True
        return False