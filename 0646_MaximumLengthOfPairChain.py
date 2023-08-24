# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        pairs.sort(key = lambda p: [p[1], p[0]])
        ans = [[None, 1] for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0] and ans[i][1] < ans[j][1] + 1:
                    ans[i] = [j, ans[j][1] + 1]
        
        return max([v[1] for v in ans])

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        cur, res = float('-inf'), 0
        for p in pairs:
            if cur < p[0]: 
                cur, res = p[1], res + 1
        return res