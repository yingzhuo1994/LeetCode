# 1st solution
# O(n) time | O(n) space
class Solution:
    def makeFancyString(self, s: str) -> str:
        lst = []
        prev = ""
        count = 0
        for ch in s:
            if ch == prev:
                count += 1
            else:
                prev = ch
                count = 1
            if count < 3:
                lst.append(ch)
        return "".join(lst)