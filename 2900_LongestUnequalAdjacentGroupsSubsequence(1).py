# 1st solution
# O(n) time | O(1) space
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        ans = []
        for i, g in enumerate(groups):
            if i == n - 1 or g != groups[i + 1]:  # i 是连续相同段的末尾
                ans.append(words[i])
        return ans