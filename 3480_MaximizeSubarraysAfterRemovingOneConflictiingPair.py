# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        groups = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            groups[a].append(b)

        ans = 0
        extra = [0] * (n + 2)
        b = [n + 1, n + 1]
        for i in range(n, 0, -1):
            b = sorted(b + groups[i])[:2]  # 维护最小 b 和次小 b
            ans += b[0] - i
            extra[b[0]] += b[1] - b[0]

        return ans + max(extra)