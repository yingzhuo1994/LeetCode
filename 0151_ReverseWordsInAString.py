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

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def reverseWords(self, s: str) -> str:
        chars = [ch for ch in s]
        n = len(chars)
        slow = 0
        for i in range(n):
            if chars[i] != " " or (i > 0 and chars[i] == " " and chars[i-1] != " "):
                chars[slow] = chars[i]
                slow += 1
        if slow == 0:
            return ""
        
        chars = chars[:slow-1] if chars[-1] == " " else chars[:slow]
        chars.reverse()

        slow, m = 0, len(chars)
        for i in range(m + 1):
            if i == m or chars[i] == " ":
                chars[slow:i] = chars[slow:i][::-1]
                slow = i + 1
        
        return "".join(chars)