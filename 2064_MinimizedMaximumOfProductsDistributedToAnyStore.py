# 1st solution
# O(m * log(k)) time | O(1) space
# where m = len(quantities), k = max(quantities) 
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        total = sum(quantities)
        if total <= n:
            return 1
        start = 1
        end = max(quantities)
        ans = end
        while start <= end:
            mid = start + (end - start) // 2
            count = 0
            for num in quantities:
                q, r = divmod(num, mid)
                if r > 0:
                    q += 1
                count += q
                if count > n:
                    break
            if count <= n:
                ans = min(ans, mid)
                end = mid - 1
            else:
                start = mid + 1
        return ans