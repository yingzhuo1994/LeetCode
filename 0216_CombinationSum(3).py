# 1st solution
# O(9! / ((9-k)! * k!)) time | O(9! / ((9-k)! * k!)) space
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.dfs(k, n, 1, [], ans)
        return ans

    def dfs(self, count, target, startValue, curLst, ans):
        if target <= 0:
            return 
        if count == 1:
            if 1 <= target <= 9 and startValue <= target:
                ans.append(curLst + [target])
            return
        for value in range(startValue, 10):
            self.dfs(count - 1, target - value, value + 1, curLst + [value], ans)

# 2nd solution, iteration
# O(9! / ((9-k)! * k!)) time | O(9! / ((9-k)! * k!)) space
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combs = [[]]
        for _ in range(k):
            combs = [[first] + comb
                     for comb in combs
                     for first in range(1, comb[0] if comb else 10)]
        return [c for c in combs if sum(c) == n]