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


# 3rd solution
# O(n^2) time | O(n^2) space
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        index_map = {num: i for i, num in enumerate(arr)}
        dp = defaultdict(lambda: defaultdict(int))
        
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if arr[i] - arr[j] >= arr[j]:
                    break
                t = index_map.get(arr[i] - arr[j], -1)
                if t == -1:
                    continue
                dp[i][j] = max(3, dp[j][t] + 1)
                ans = max(ans, dp[i][j])
        
        return ans