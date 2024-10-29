# 1st solution
# O(n * 2^n) time | O(n) space
class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]

        last = self.validStrings(n - 1)
        ans = []
        for s in last:
            ans.append(s + "1")
            if s[-1] == "1":
                ans.append(s + "0")
        return ans