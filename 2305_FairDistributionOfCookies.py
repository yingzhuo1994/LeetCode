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
        