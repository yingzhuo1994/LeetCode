# 1st solution
# O(m * log(m)) time | O(m) space
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(score), len(score[0])
        lst = [i for i in range(m)]
        lst.sort(key=lambda i: -score[i][k])
        return [score[i] for i in lst]