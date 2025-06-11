# 1st solution
# O(nm^2) time | O(m) space
# where n = len(s) and m = len(set(s))
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        s = list(map(int, s))
        ans = -inf
        for x in range(5):
            for y in range(5):
                if y == x:
                    continue
                cur_s = [0] * 5
                pre_s = [0] * 5
                min_s = [[inf, inf], [inf, inf]]
                left = 0
                for i, v in enumerate(s):
                    cur_s[v] += 1
                    r = i + 1
                    while r - left >= k and cur_s[x] > pre_s[x] and cur_s[y] > pre_s[y]:
                        p, q = pre_s[x] & 1, pre_s[y] & 1
                        min_s[p][q] = min(min_s[p][q], pre_s[x] - pre_s[y])
                        pre_s[s[left]] += 1
                        left += 1
                    if r >= k:
                        ans = max(ans, cur_s[x] - cur_s[y] - min_s[cur_s[x] & 1 ^ 1][cur_s[y] & 1])
        return ans