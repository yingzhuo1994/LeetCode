# 1st solution, DFS
# O(n!) time | O(n) space
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        def dfs(idx, lst):
            if idx == n:
                return True
            for num in range(1, 10):
                if num in lst:
                    continue
                if pattern[idx] == "I":
                    if num > lst[-1]:
                        lst.append(num)
                        if dfs(idx + 1, lst):
                            return True
                        lst.pop()
                else:
                    if num < lst[-1]:
                        lst.append(num)
                        if dfs(idx + 1, lst):
                            return True
                        lst.pop()
            return False
        for i in range(1, 10):
            lst = [i]
            if dfs(0, lst):
                break
        return "".join(map(str, lst))
