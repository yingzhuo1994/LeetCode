# 1st solution
# O(n) time | O(n) space
class Solution:
    def finalString(self, s: str) -> str:
        ans = []
        for ch in s:
            if ch == "i":
                ans.reverse()
            else:
                ans.append(ch)
        return "".join(ans)