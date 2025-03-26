# 1st solution
# O(n) time | O(n) space
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        ans = 0
        values = set()
        i = 1
        while len(values) < n:
            if i < k:
                d = k - i
                if d not in values:
                    values.add(i)
                    ans += i
            else:
                values.add(i)
                ans += i
            i += 1
        return ans


# 2nd solution
# O(1) time | O(1) space
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        m = min(k // 2, n)
        return (m * (m + 1) + (k * 2 + n - m - 1) * (n - m)) // 2