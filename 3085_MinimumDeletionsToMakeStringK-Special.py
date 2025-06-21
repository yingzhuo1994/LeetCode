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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = Counter(word)
        freqs = list(cnt.values())
        freqs.sort()
        total = sum(freqs)
        ans = total
        n = len(freqs)
        curSum_1 = curSum_2 = 0
        i = 0
        j = i
        while j < n:
            d = freqs[j] - freqs[i] - k
            if d <= 0:
                curSum_2 += freqs[j]
                j += 1
            else:
                diff = curSum_1 + total - curSum_2 - (freqs[i] + k) * (n - j)
                ans = min(ans, diff)
                curSum_1 += freqs[i]
                i += 1
        ans = min(ans, curSum_1)
        return ans