# 1st solution
# O(t) time | O(1) space
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        for _ in range(t):
            tmp = [0] * 26
            for i in range(26):
                if i == 25:
                    tmp[0] = (tmp[0] + cnt[i]) % MOD
                    tmp[1] = (tmp[1] + cnt[i]) % MOD
                else:
                    tmp[i + 1] = (tmp[i + 1] + cnt[i]) % MOD
            cnt = tmp

        return sum(cnt) % MOD