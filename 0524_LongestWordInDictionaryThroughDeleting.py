# 1st solution
# O(kn) time | O(1) space
# where n = len(dictionary) and k = len(s)
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def contains(s, t):
            j = 0
            for i in range(len(s)):
                if j >= len(t):
                    return True
                if s[i] == t[j]:
                    j += 1
            return j == len(t)
        
        ans = ""
        for word in dictionary:
            if contains(s, word):
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans) and word < ans:
                    ans = word
        return ans