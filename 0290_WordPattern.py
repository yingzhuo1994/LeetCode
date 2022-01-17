# 1st solution
# O(n) time | O(1) space
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        patternToWord = {}
        wordToPattern = {}
        if len(pattern) != len(words):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in patternToWord:
                if patternToWord[pattern[i]] != words[i]:
                    return False
            elif words[i] in wordToPattern:
                if wordToPattern[words[i]] != pattern[i]:
                    return False
            else:
                patternToWord[pattern[i]] = words[i]
                wordToPattern[words[i]] = pattern[i]
        return True