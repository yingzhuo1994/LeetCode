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
