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

# 2nd solution
# O(ksn) time | O(ksn) space
# where n is the length of words, k is the largest word length, and s is the unique word length of words
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dic = {word: i for i, word in enumerate(words)}
        palindromLst = []
        possibleLength = set()
        for word in words:
            possibleLength.add(len(word))
        if 0 in possibleLength:
            possibleLength.remove(0)
        possibleLength = sorted(list(possibleLength))
        ans = []
        hasEmpty = False
        for word in words:
            i = dic[word]
            if word == "":
                hasEmpty = True
            elif self.isPalindrome(word):
                palindromLst.append(word)
            elif word[::-1] in dic:
                j = dic[word[::-1]]
                ans.append([i, j])
            
            candidates = self.getCandidates(word, possibleLength)
            for candidate, place in candidates:
                if candidate in dic:
                    j = dic[candidate]
                    if place == "left":
                        ans.append([i, j])
                    else:
                        ans.append([j, i])
        
        if hasEmpty:
            i = dic[""]
            for word in palindromLst:
                j = dic[word]
                ans.append([i, j])
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
    
    def getCandidates(self, word, possibleLength):
        n = len(word)
        candidates = []
        idx = bisect.bisect_left(possibleLength, n)
        # in the left
        for i in range(idx):
            L = possibleLength[i]
            if self.isPalindrome(word[L:]):
                candidate = word[:L]
                candidates.append([candidate[::-1], "left"])

        # in the right
        for i in range(idx):
            L = possibleLength[i]
            if self.isPalindrome(word[:-L]):
                candidate = word[-L:]
                candidates.append([candidate[::-1], "right"])
        return candidates