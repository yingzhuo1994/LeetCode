class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def smoother(x, y):
            count = 0
            value = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    i = x + dx
                    j = y + dy
                    if 0 <= i < len(img) and 0 <= j < len(img[0]):
                        count += 1
                        value += img[i][j]
            return floor(value / count)
        
        m, n = len(img), len(img[0])

        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = smoother(i, j)
        
        return ans