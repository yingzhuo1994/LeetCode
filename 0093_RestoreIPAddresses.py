# 1st solution
# O(n^3) time | O(n^4) space
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:
            return []
        
        ans = []
        def dfs(idx, stack):
            if idx == n:
                if len(stack) == 4:
                    ans.append(".".join([str(num) for num in stack]))
                return
            if len(stack) >= 4:
                return
            if int(s[idx]) == 0:
                dfs(idx + 1, stack + [int(s[idx])])
                return

            for i in range(idx + 1, min(idx + 4, n + 1)):
                num = int(s[idx:i])
                if num <= 255:
                    dfs(i, stack + [num])
        dfs(0, [])
        return ans