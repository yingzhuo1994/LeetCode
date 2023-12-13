# 1st solution
# O(n) time | O(n) space
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        lst = list(s)
        start, end = 0, len(lst) - 1
        while start < end:
            if lst[start] < lst[end]:
                lst[end] = lst[start]
            elif lst[start] > lst[end]:
                lst[start] = lst[end]
            start += 1
            end -= 1
        return "".join(lst)