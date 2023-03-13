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

# 2nd solution, Top-Down
# O(^4) time | O(n^3) space
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(l, r, k):
            # dp(i,j,k) means the max points you can earn between boxes "i" and "j", with "k" boxes before i that has the same color as "i".
            if l > r: 
                return 0
            
            while l < r and boxes[l] == boxes[l+1]:
                l += 1
                k += 1
                
            ans = (k + 1) * (k + 1) + dp(l + 1, r, 0)
            
            for m in range(l + 1, r + 1):
                if boxes[m] == boxes[l] and boxes[m - 1] != boxes[l]:
                    ans = max(ans, dp(l + 1, m - 1, 0) + dp(m, r, k + 1))
                    
            return ans
             
        return dp(0, len(boxes)-1, 0)