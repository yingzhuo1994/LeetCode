class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s) - 1
        while p1 <= p2:
            if s[p1] == ' ' or s[p1] in string.punctuation:
                p1 += 1
                continue
            if s[p2] == ' ' or s[p2] in string.punctuation:
                p2 -= 1
                continue
            if s[p1].lower() != s[p2].lower():
                return False
            else:
                p1 += 1
                p2 -= 1
        return True
