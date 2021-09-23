class Solution:
    # 1st solution
    # O(n) time | O(n) space
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        
        n = len(palindrome)
        for i in range(n - 1):
            if palindrome[i] == 'a' or i == n // 2:
                continue
            return palindrome[:i] + 'a' + palindrome[i+1:]
        if palindrome[-1] == 'a':
            return palindrome[:-1] + 'b'
            