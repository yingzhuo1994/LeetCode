# 1st solution, brute-force method, TLE
# O(n^3) time | O(1) space
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        banned = {tuple(mine) for mine in mines}
        ans = 0
        for r in range(n):
            for c in range(n):
                k = 0
                while (k <= r < n-k and k <= c < n-k and
                        (r-k, c) not in banned and
                        (r+k, c) not in banned and
                        (r, c-k) not in banned and
                        (r, c+k) not in banned):
                    k += 1
                ans = max(ans, k)
        return ans

# 2nd solution
# O(n^2) time | O(n^2) space
class Solution: 
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        baned = {tuple(mine) for mine in mines}
        dp = [[0] * n for _ in range(n)]
        ans = 0
        
        for r in range(n):
            count = 0
            for c in range(n):
                count = 0 if (r,c) in baned else count+1
                dp[r][c] = count
            
            count = 0
            for c in range(n-1, -1, -1):
                count = 0 if (r,c) in baned else count+1
                if count < dp[r][c]: dp[r][c] = count
        
        for c in range(n):
            count = 0
            for r in range(n):
                count = 0 if (r,c) in baned else count+1
                if count < dp[r][c]: dp[r][c] = count
            
            count = 0
            for r in range(n-1, -1, -1):
                count = 0 if (r, c) in baned else count+1
                if count < dp[r][c]: dp[r][c] = count
                if dp[r][c] > ans: ans = dp[r][c]
        
        return ans