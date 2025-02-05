# 1st solution
# O(n^2 * log(n)) time | O(1) space
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        def dfs(i, j):
            a, b = arr[i], arr[j]
            c = a + b
            k = bisect.bisect_left(arr, c, lo=j)
            if k < len(arr) and arr[k] == c:
                return dfs(j, k) + 1
            return 0
        ans = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                cnt = dfs(i, j)
                if cnt > 0:
                    ans = max(ans, cnt + 2)
        return ans


# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        vals = set(arr)
        ans = 0
        n = len(arr)
        for i in range(n):
            a = arr[i]
            for j in range(i + 1, n):
                b = arr[j]
                c = a + b
                cnt = 2
                while c in vals:
                    cnt += 1
                    b, c = c, b + c
                if cnt > 2:
                    ans = max(ans, cnt)
        return ans