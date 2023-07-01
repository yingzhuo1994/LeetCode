# 1st solution, MLE
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        stack = [[0 for _ in range(k)]]
        for i in range(len(cookies)):
            newStack = []
            for j in range(k):
                for lst in stack:
                    newLst = lst[:]
                    newLst[j] += cookies[i]
                    newStack.append(newLst)
            stack = newStack
        ans = float("inf")
        for lst in stack:
            ans = min(ans, max(lst))
        
        return ans

# 2nd solution
# O(n^k) time | O(n) space
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        stack = [0 for _ in range(k)]
        n = len(cookies)
        self.ans = float("inf")
        def dfs(idx):
            if idx >= n:
                self.ans = min(self.ans, max(stack))
                return
            if max(stack) >= self.ans:
                return
            for i in range(k):
                stack[i] += cookies[idx]
                dfs(idx + 1)
                stack[i] -= cookies[idx]
                if stack[i] == 0:
                    break
        dfs(0)                
        return self.ans