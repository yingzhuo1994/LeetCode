# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for word1 in words:
            for word2 in words:
                if word1 != word2 and word1 in word2:
                    ans.append(word1)
                    break
        return ans