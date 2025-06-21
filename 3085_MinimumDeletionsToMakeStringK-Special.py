# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        freqs = list(cnt.values())
        freqs.sort()
        total = sum(freqs)
        ans = total
        n = len(freqs)
        curSum = 0
        for i in range(n):
            diff = curSum
            for j in range(i + 1, n):
                d = freqs[j] - freqs[i] - k
                if d > 0:
                    diff += d
            curSum += freqs[i]
            ans = min(ans, diff)
        return ans