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
