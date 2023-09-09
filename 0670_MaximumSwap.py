# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        ans = num
        for i in range(len(s)):
            for j in range(i):
                new = s[:j] + s[i] + s[j+1:i] + s[j] + s[i+1:]
                k = int(new)
                if k > ans:
                    ans = k
        return ans