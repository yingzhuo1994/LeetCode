class Solution:
    # 1st solution
    # O(n) time | O(n) space
    def reverseWords(self, s: str) -> str:
        lst = []
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                self.reverse(lst, start, i - 1)
                start = i + 1
            lst.append(s[i])
        self.reverse(lst, start, len(s) - 1)
        return "".join(lst)
    
    def reverse(self, lst, start, end):
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1