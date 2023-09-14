class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        grid = [[False for _ in range(9)] for _ in range(8)]
        ans = []

        for a, b in queens:
            grid[a][b] = True
        
        directions = [[0, 1], [0, -1], [1 ,0], [-1, 0], [1, 1], [1, -1], [-1, -1], [-1, 1]]

        for dx, dy in directions:
            for L in range(1, 8):
                x = king[0] + dx * L
                y = king[1] + dy * L
                if x < 0 or x >= 8 or y < 0 or y >= 8:
                    break
                if grid[x][y]:
                    ans.append([x, y])
                    break
        
        return ans
