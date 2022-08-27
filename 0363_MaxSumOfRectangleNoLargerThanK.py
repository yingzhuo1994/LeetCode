# 1st solution
# O(m^2*n^2) time | O(mn) space
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        for row in matrix:
            for j in range(1, n):
                row[j] += row[j-1]
        
        ans = float("-inf")

        for y1 in range(n):
            for y2 in range(y1, n):
                curSum = 0
                dic = set([0])
                for x in range(m):
                    if y1 > 0:
                        last = matrix[x][y1-1]
                    else:
                        last = 0
                    curSum += matrix[x][y2] - last
                    if curSum - k in dic:
                        return k
                    for lastSum in dic:
                        diff = curSum - lastSum
                        if diff < k:
                            ans = max(ans, diff)
                    dic.add(curSum)
        return ans
                    

# 2nd solution
# O(m^2*n^2) time | O(mn) space
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def countRangeSum(nums, U):
            SList, ans = [0], -float("inf")
            for s in accumulate(nums):
                idx = bisect.bisect_left(SList, s - U) 
                if idx < len(SList): ans = max(ans, s - SList[idx])        
                bisect.insort(SList, s)
            return ans
        
        m, n, ans = len(matrix), len(matrix[0]), -float("inf")
        
        for i, j in product(range(1, m), range(n)):
            matrix[i][j] += matrix[i-1][j]
                
        matrix = [[0]*n] + matrix
        
        for r1, r2 in combinations(range(m + 1), 2):
            row = [j - i for i, j in zip(matrix[r1], matrix[r2])]
            ans = max(ans, countRangeSum(row, k))
            
        return ans