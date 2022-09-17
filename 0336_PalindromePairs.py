# 1st solution
# O(k * n^2) time | O(n^2) space
# where n is the length of words, and k is the largest word length
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        ans = []
        for i in range(n):
            for j in range(i + 1, n):
                if self.isPalindrome(words[i] + words[j]):
                    ans.append([i, j])
                if self.isPalindrome(words[j] + words[i]):
                    ans.append([j, i])
        
        return ans
    
    def isPalindrome(self, word):
        i, j = 0, len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True