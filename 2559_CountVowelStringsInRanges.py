# 1st solution
# O(n + k) time | O(n + k) space
# where n = len(words), and k = len(queries)
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = "aeiou"
        n = len(words)
        dp = [0 for _ in range(n + 1)]
        for i, word in enumerate(words):
            hasVowel = word[0] in vowels and word[-1] in vowels
            dp[i] = dp[i-1] + hasVowel
        return [dp[r] - dp[l-1] for l, r in queries]