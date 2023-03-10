# 1st solution, TLE
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        memo = {}
        def dfs(lst):
            if len(lst) <= 1:
                return len(lst)
            key = tuple(lst)
            if key in memo:
                return memo[key]
            ans = 0
            i = 0
            while i < len(lst):
                start = i
                j = start
                while j < len(lst) and lst[j] == lst[start]:
                    j += 1
                k = j - i
                ans = max(ans, k * k + dfs(lst[:start] + lst[j:]))
                i = j
            memo[key] = ans
            return ans
        return dfs(boxes)

# 2nd solution
# O(^4) time | O(n^3) space
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j, k):
            # dp(i,j,k) means the max points you can earn between boxes "i" and "j", with "k" boxes before i that has the same color as "i".
            if i > j: 
                return 0
            indx = [m for m in range(i+1, j+1) if boxes[m] == boxes[i]]
            ans = (k+1)**2 + dp(i+1, j, 0)
            return max([ans] + [dp(i+1, m-1, 0) + dp(m, j, k+1) for m in indx])   
            
        return dp(0, len(boxes)-1, 0)