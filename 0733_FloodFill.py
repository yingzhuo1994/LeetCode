class Solution:
    # O(n) time | O(n) space
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        if originalColor == newColor:
            return image
        self.dfs(image, sr, sc, originalColor, newColor)
        return image
    
    def dfs(self, image, i, j, originalColor, newColor):
        if image[i][j] != originalColor:
            return
        image[i][j] = newColor 
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            row, col = i + x, j + y
            if 0 <= row < len(image) and 0 <= col < len(image[0]):
                self.dfs(image, row, col, originalColor, newColor)