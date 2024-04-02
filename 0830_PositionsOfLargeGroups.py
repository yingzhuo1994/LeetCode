# 1st solution
# O(n) time | O(n) space
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        start = 0
        last = None
        for i, ch in enumerate(s):
            if ch == last:
                continue
            else:
                count = i - start
                if count >= 3:
                    ans.append([start, i - 1])
                start = i
                last = ch
        if s[-1] == last and len(s) - start >= 3:
            ans.append([start, len(s) - 1])
        return ans
        