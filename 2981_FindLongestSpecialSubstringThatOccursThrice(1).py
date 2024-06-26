# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def maximumLength(self, s: str) -> int:
        dic = {}
        start = -1
        last = None
        for i, ch in enumerate(s):
            if ch != last:
                start = i
                last = ch
            sub = s[start:i+1]
            if sub in dic:
                continue
            dic[sub] = 1
            for j in range(i - len(sub) + 2, len(s) - len(sub) + 1):
                if s[j:j+len(sub)] == sub:
                    dic[sub] += 1
        return max([len(sub) for sub in dic if dic[sub] >= 3] + [-1])


# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maximumLength(self, s: str) -> int:
        groups = defaultdict(list)
        cnt = 0
        for i, ch in enumerate(s):
            cnt += 1
            if i + 1 == len(s) or ch != s[i + 1]:
                groups[ch].append(cnt)  # 统计连续字符长度
                cnt = 0

        ans = 0
        for a in groups.values():
            a.sort(reverse=True)
            a.extend([0, 0])  # 假设还有两个空串
            ans = max(ans, a[0] - 2, min(a[0] - 1, a[1]), a[2])

        return ans if ans else -1