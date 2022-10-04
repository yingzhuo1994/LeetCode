# 1st solution
# O(n) space | O(n) time 
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = Counter("qwertyuiop")
        secondRow = Counter("asdfghjkl")
        thirdRow = Counter("zxcvbnm")
        ans = []
        for word in words:
            wordCount = Counter(word)
            if all(ch.lower() in firstRow for ch in wordCount):
                ans.append(word)
                continue
            if all(ch.lower() in secondRow for ch in wordCount):
                ans.append(word)
                continue
            if all(ch.lower() in thirdRow for ch in wordCount):
                ans.append(word)
                continue
        return ans

# 2nd solution
# O(n) space | O(n) time 
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = set("qwertyuiop")
        secondRow = set("asdfghjkl")
        thirdRow = set("zxcvbnm")
        ans = []
        for word in words:
            wordSet = set(word.lower())
            if wordSet <= firstRow or wordSet <= secondRow or wordSet <= thirdRow:
                ans.append(word)
        return ans