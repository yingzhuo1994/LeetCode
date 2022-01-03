# 1st solution
# O(n) time | O(n) space
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        table = [[0, 0] for _ in range(n + 1)]
        for a, b in trust:
            table[a][0] += 1
            table[b][1] += 1
        judges = []
        for i in range(1, n + 1):
            if table[i][0] == 0 and table[i][1] == n - 1:
                judges.append(i)
        if len(judges) == 1:
            return judges[0]
        else:
            return -1 
        