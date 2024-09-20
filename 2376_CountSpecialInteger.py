# 1st solution
# O(m * D * 2^D) time | O(m * 2^D) space
# where m = len(str(n)), D = 10
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        n = min(n, 9876543210)
        lst = list(map(int, list(str(n))))
        @cache
        def dfs(idx, zero, is_limit, mask):
            if idx == len(lst):
                if mask != 1:
                    return 1
                else:
                    return 0
            limit = 9 if not is_limit else min(9, lst[idx])
            count = 0
            for d in range(limit + 1):
                if (1 << d) & mask:
                    continue
                if zero and d == 0:
                    newMask = 0
                else:
                    newMask = mask | (1 << d)
                v = dfs(idx + 1, zero and d == 0, is_limit and d == lst[idx], newMask)
                count += v
            return count
        return dfs(0, True, True, 0) - 1
