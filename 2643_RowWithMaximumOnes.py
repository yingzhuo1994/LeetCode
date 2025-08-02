# 1st solution
# O(mn) time | O(1) space
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        idx = 0
        ans = 0
        for i, row in enumerate(mat):
            cnt = sum(row)
            if cnt > ans:
                ans = cnt
                idx = i
        return [idx, ans]