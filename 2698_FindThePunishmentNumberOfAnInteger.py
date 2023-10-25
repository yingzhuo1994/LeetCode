# 1st solution
class Solution:
    def punishmentNumber(self, n: int) -> int:
        @cache
        def dfs(s, idx, target):
            if idx == len(s):
                return target == 0
            for j in range(idx + 1, len(s) + 1):
                num = int(s[idx:j])
                if num > target:
                    continue
                if dfs(s, j, target - num):
                    return True
            return False
        
        def helper(number):
            sq = number * number
            s = str(sq)
            return dfs(s, 0, number)
        
        ans = 0
        for num in range(1, n + 1):
            if helper(num):
                ans += num * num
        return ans