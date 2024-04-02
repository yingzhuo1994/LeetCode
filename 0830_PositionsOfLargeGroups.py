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

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i, j, n = 0, 0, len(s)
        res = []
        
        while i < n:
            while j < n and s[j] == s[i]:
                j += 1
            if j - i >= 3:
                res.append([i, j - 1])
            i = j
        
        return res