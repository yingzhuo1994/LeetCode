# 1st solution
# O(n * log(n)) time | O(D * log(n)) space
class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = defaultdict(int)
        max_cnt = ans = 0
        for i in range(1, n + 1):
            ds = sum(map(int, str(i)))
            cnt[ds] += 1
            # 维护 max_cnt 以及 max_cnt 的出现次数
            if cnt[ds] > max_cnt:
                max_cnt = cnt[ds]
                ans = 1
            elif cnt[ds] == max_cnt:
                ans += 1
        return ans