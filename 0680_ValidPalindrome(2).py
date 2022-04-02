# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if self.isPalindrome(s):
            return True
        for i in range(len(s)):
            newString = s[:i] + s[i+1:]
            if self.isPalindrome(newString):
                return True
        return False
    
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        return self.dfs(s, left, right, 1)
    
    def dfs(self, s, left, right, deleteCount):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif deleteCount > 0:
                if self.dfs(s, left + 1, right, deleteCount - 1) or self.dfs(s, left, right - 1, deleteCount - 1):
                    return True
                else:
                    return False
            else:
                return False
        return True

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True
    
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# 4th solution
# O(n) time | O(1) space
class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.isPalindrome(s, 0, len(s) - 1, 1)
    
    def isPalindrome(self, s, left, right, deleteCount):
        if deleteCount < 0:
            return False
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right, deleteCount - 1) or self.isPalindrome(s, left, right - 1, deleteCount - 1)
            left += 1
            right -= 1
        return True