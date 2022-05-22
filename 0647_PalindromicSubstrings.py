# 1st solution
# O(n^2) time | O(1) space
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += self.countPalindrome(s, i, i)
            ans += self.countPalindrome(s, i, i + 1)
        return ans  

    def countPalindrome(self, s, left, right):
        count = 0
        while 0 <= left and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
            
        return count