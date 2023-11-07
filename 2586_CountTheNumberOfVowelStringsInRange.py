# 1st solution
# O(n) time | O(1) space
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        vowels = {"a", "e", "i", "o", "u"}
        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                ans += 1
        return ans