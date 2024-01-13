# 1st solution
# O(n) time | O(1) space
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count1 = Counter(s)
        count2 = Counter(t)
        ans = 0
        for ch in count2:
            if ch in count1:
                ans += max(0, count2[ch] - count1[ch])
            else:
                ans += count2[ch]
        return ans