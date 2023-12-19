# 1st solution
# O(n * log(m)) time | O(1) space
# where m = len(mat), n = len(mat[0])
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        left, right = 0, len(mat) - 2
        while left <= right:
            i = (left + right) // 2
            mx = max(mat[i])
            if mx > mat[i + 1][mat[i].index(mx)]:
                right = i - 1  # 峰顶行号 <= i
            else:
                left = i + 1  # 峰顶行号 > i
        i = left
        return [i, mat[i].index(max(mat[i]))]