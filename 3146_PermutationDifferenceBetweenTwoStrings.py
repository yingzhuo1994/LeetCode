# 1st solution
# O(1) time | O(1) space
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dic = {ch: i for i, ch in enumerate(s)}
        ans = sum(abs(i - dic[ch]) for i, ch in enumerate(t))
        return ans