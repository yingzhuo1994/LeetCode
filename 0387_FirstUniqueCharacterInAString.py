class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 1st solution
        # O(n) time | O(n) space
        for i, ch in enumerate(s):
            if ch not in s[:i] and ch not in s[i+1:]:
                return i
        return -1

        # 2nd solution
        # O(n) time | O(1) space
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
