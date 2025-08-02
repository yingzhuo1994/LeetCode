# 1st solution
# O(n + q * log(n)) time | O(n) space
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        left = [0] * n
        pre = [0] * (n + 1)
        cnt = [0, 0]
        l = 0
        for i, c in enumerate(s):
            cnt[ord(c) & 1] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[ord(s[l]) & 1] -= 1
                l += 1
            left[i] = l  # 记录合法子串右端点 i 对应的最小左端点 l
            # 计算 i-left[i]+1 的前缀和
            pre[i + 1] = pre[i] + i - l + 1

        ans = []
        for l, r in queries:
            j = bisect_left(left, l, l, r + 1)  # 如果区间内所有数都小于 l，结果是 j=r+1
            ans.append(pre[r + 1] - pre[j] + (j - l + 1) * (j - l) // 2)
        return ans