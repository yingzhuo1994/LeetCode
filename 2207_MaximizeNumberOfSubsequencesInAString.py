# 1st solution
# O(n) time | O(1) space
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        cnt1 = 0
        cnt2 = 0
        ans = 0
        for ch in text:
            if ch == pattern[0]:
                if pattern[0] == pattern[1]:
                    ans += cnt1
                cnt1 += 1
            elif ch == pattern[1]:
                ans += cnt1
                cnt2 += 1
        return ans + max(cnt1, cnt2)