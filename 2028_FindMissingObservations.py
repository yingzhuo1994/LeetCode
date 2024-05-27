# 1st solution
# O(m + n) time | O(n) space
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m + n)
        target = total - sum(rolls)
        if target > 6 * n or target < n:
            return []
        ans = []
        k = n
        for val in reversed(range(1, 7)):
            q, r = divmod(target, val)
            while k - q > r:
                q -= 1
                r += val
            if q > 0:
                ans += [val] * q
                target -= q * val
                k -= q
        return ans


# 2nd solution
# O(m + n) time | O(n) space
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        rem = mean * (n + len(rolls)) - sum(rolls)
        if not n <= rem <= n * 6:
            return []
        avg, extra = divmod(rem, n)
        return [avg + 1] * extra + [avg] * (n - extra)