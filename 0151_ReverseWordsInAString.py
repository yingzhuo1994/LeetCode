# 1st solution
# O(n) time | O(n) space
class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                stack.append(s[start:i])
                start = i + 1
            elif i == len(s) - 1:
                stack.append(s[start:i+1])
        stack = list(reversed(stack))
        result = ""
        for word in stack:
            if word not in ("", " "):
                result += word + " "
        return result[:-1]


# 2nd solution
# O(n) time | O(n) space
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])