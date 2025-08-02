# 1st solution
# O(n) time | O(n) space
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total = sum(skill)
        n = len(skill)
        target, r = divmod(total, n // 2)
        if r != 0:
            return -1
        cnt = Counter(skill)
        ans = 0
        for a in cnt:
            b = target - a
            if a == b:
                if cnt[a] & 1:
                    return -1
                k = cnt[a] // 2
                cnt[a] = 0
                ans += k * a * a
            else:
                if cnt[b] != cnt[a]:
                    return -1
                ans += cnt[a] * a * b
                cnt[a] = 0
                cnt[b] = 0
        return ans