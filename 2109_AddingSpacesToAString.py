# 1st solution
# O(n) time | O(n) space
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        lst = []
        start = 0
        for i in spaces:
            lst.append(s[start:i])
            start = i
        lst.append(s[start:])
        return " ".join(lst)