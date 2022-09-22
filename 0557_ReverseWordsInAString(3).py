# 1st solution
# O(n) time | O(n) space
class Solution:
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

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i, word in enumerate(words):
            words[i] = word[::-1]
        return " ".join(words)