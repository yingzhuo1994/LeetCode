class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)
        
        ans = []
        for word in words:
            if trie.hasConcatenated(word):
                ans.append(word)
        return ans

class Trie:
    def __init__(self):
        self.root = {}
        self.end = "*"
    
    def add(self, word):
        dic = self.root
        for ch in word:
            if ch not in dic:
                dic[ch] = {}
            dic = dic[ch]
        dic[self.end] = True
    
    def hasConcatenated(self, word, idx=0):
        if idx == len(word):
            return True
        for i in range(idx, len(word)):
            curWord = word[idx:i+1]
            if curWord == word:
                return False
            if self.isContaind(curWord):
                if self.hasConcatenated(word, i + 1):
                    return True
        return False
        
    
    def isContaind(self, word):
        dic = self.root
        for ch in word:
            if ch not in dic:
                return False
            dic = dic[ch]
        return self.end in dic
