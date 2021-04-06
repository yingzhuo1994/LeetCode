class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        start = ord('A') - 1
        num = 0
        for ch in columnTitle:
            num = 26 * num + ord(ch) - start
        return num
