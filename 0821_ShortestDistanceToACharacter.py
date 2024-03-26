# 1st solution
# O(n) time | O(n) space
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [inf for _ in s]
        last = 0
        for i, ch in enumerate(s):
            if ch == c:
                dist = 0
                for j in reversed(range(last, i + 1)):
                    ans[j] = min(ans[j], dist)
                    dist += 1
                
                dist = 1
                for j in range(i + 1, len(s)):
                    if s[j] == c:
                        break
                    ans[j] = min(ans[j], dist)
                    dist += 1
                last = i
        return ans
            