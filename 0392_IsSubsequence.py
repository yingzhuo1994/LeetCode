# 1st solution
# O(n) time | O(1) space
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

# 2nd solution, for follow up
# O(n) time | O(1) space
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = defaultdict(list)
        for i, c in enumerate(t):
            idx[c].append(i)
        prev = 0
        for i, c in enumerate(s):            
            j = bisect.bisect_left(idx[c], prev)
            if j == len(idx[c]): return False
            prev = idx[c][j] + 1
        return True  