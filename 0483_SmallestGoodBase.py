# 1st solution
# O((log(n))^2) time | O(1) space
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_len = len(bin(n)) - 2
        for m in reversed(range(1, max_len + 1)):
            lo = 2
            hi = n - 1     # or hi = int(pow(n, pow(m - 1, -1))) and only need check hi
            while lo <= hi:
                mid = (lo + hi) // 2
                num = (pow(mid, m) - 1) // (mid - 1)
                if num < n:
                    lo = mid + 1
                elif num > n:
                    hi = mid - 1
                else:
                    return str(mid)
        return str(n - 1)

# 2nd solution
# O(log(n)) time | O(1) space
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        m_max = int(math.log(n, 2))
        
        for m in range(m_max, 1, -1):
            k = int(n**(1/m))
            if (k**(m+1) - 1)  == n*(k-1):
                return str(k)
        return str(n-1)     