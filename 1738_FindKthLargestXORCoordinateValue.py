# 1st solution
# O(mn * log(k)) time | O(mn) space
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        mHeap = []
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i][j] ^ dp[i+1][j] ^ dp[i][j+1] ^ matrix[i][j]
                heappush(mHeap, dp[i+1][j+1])
                if len(mHeap) > k:
                    heappop(mHeap)

        return mHeap[0]
