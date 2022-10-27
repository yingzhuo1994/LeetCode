# 1st solution
# O(n^4) time | O(1) space
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ans = 0
        n = len(img1)
        for dx in range(-n + 1, n):
            for dy in range(-n + 1, n):
                overlap = self.translateCompare(img1, img2, dx, dy)
                ans = max(ans, overlap)
        return ans
    
    def translateCompare(self, img1, img2, dx, dy):
        n = len(img1)
        rowStart = max(-dx, 0)
        rowEnd =  min(n - 1, n  - 1 - dx)
        colStart = max(-dy, 0)
        colEnd = min(n - 1, n - 1 - dy)
        
        count = 0
        for i in range(rowStart, rowEnd + 1):
            for j in range(colStart, colEnd + 1):
                if img1[i][j] == img2[i+dx][j+dy] and img1[i][j] == 1:
                    count += 1
        return count