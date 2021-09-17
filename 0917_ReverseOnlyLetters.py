class Solution:
    # 1st solution
    # O(n) time | O(n) space
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1
        lst = list(s)
        while left <= right:
            if not self.checkLetter(lst[left]):
                left += 1
                continue
            if not self.checkLetter(lst[right]):
                right -= 1
                continue
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        return ''.join(lst)

    def checkLetter(self, ch):
        if ord('A') <= ord(ch) <= ord('Z') or ord('a') <= ord(ch) <= ord('z'):
            return True
        return False

    # 2nd solution
    # O(n) time | O(n) space
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)

    # 3rd solution
    # O(n) time | O(n) space
    def reverseOnlyLetters(self, s: str) -> str:
        ans = []
        j = len(ans) - 1
        for i, x in enumerate(s):
            if x.isalpha():
                while not s[j].isalpha():
                    j -= 1
                ans.append(s[j])
                j -= 1
            else:
                ans.append(x)
        
        return "".join(ans)