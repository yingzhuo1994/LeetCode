class Solution:
    # 1st solution
    # O(n) time | O(n) space
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = []
        n = len(s)
        shift_num = 0
        for i in reversed(range(n)):
            shift_num += shifts[i]
            shift_num %= 26
            letter_ord = ord('a') + (ord(s[i]) + shift_num - ord('a')) % 26
            letter = chr(letter_ord)
            res.append(letter)
        return ''.join(res[::-1])