# 1st solution
# O(n) time | O(n) space
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        cnt = Counter()
        n = len(word)
        for i in range(0, n, k):
            cnt[word[i:i+k]] += 1
        freq = max(cnt.values())
        return n // k - freq