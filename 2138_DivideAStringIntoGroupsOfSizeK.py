# 1st solution
# O(n) time | O(n) space
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(0, len(s), k):
            if i + k > len(s):
                ans.append(s[i:])
                ans[-1] += fill * (i + k - len(s))
            else:
                ans.append(s[i:i+k])
        return ans