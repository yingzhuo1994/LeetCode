# 1st solution, MLE
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        
        @cache
        def dfs(node, end):
            if node >= n:
                return 0
            if rides[node][0] < end:
                return dfs(node + 1, end)
            ans = rides[node][1] - rides[node][0] + rides[node][2]

            return max(ans + dfs(node + 1, rides[node][1]), dfs(node + 1, end))
        
        return dfs(0, -1)

# 2nd solution
# O(n + m) time | O(n + m) space
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        groups = defaultdict(list)
        for start, end, tip in rides:
            groups[end].append((start, end - start + tip))

        f = [0] * (n + 1)
        for i in range(2, n + 1):
            f[i] = f[i - 1]
            if i in groups:
                f[i] = max(f[i], max(f[s] + t for s, t in groups[i]))
        return f[n]