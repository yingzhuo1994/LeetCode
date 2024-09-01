# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        mat = []
        for i in range(0, m * n, n):
            mat.append(original[i:i+n])
        return mat