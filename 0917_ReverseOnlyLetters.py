class Solution:
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