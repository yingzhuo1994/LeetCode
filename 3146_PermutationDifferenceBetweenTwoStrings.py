# 1st solution
# O(1) time | O(1) space
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dic = {ch: i for i, ch in enumerate(s)}
        ans = 0
        for i, ch in enumerate(t):
            ans += abs(i - dic[ch])
        return ans