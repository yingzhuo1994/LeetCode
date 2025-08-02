# 1st solution
# O(n^2) time | O(1) space
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    ans += 1
        return ans