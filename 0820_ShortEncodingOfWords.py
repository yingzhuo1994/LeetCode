# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        wordsSet = set()
        for word in words:
            wordsSet.add(word)
        
        wordsLst = sorted(list(wordsSet), key=len)
        trie = Trie()
        ans = 0
        for i in reversed(range(len(wordsLst))):
            word = wordsLst[i]
            if trie.search(word):
                continue
            else:
                trie.add(word)
                ans += len(word) + 1
        
        return ans

class Trie:
    def __init__(self):
        self.root = {}
        self.end = "#"
    
    def add(self, word):
        dic = self.root
        for i in reversed(range(len(word))):
            ch = word[i]
            if ch not in dic:
                dic[ch] = {}
            dic = dic[ch]
        dic[self.end] = word
    
    def search(self, word):
        dic = self.root
        for i in reversed(range(len(word))):
            ch = word[i]
            if ch not in dic:
                return False
            dic = dic[ch]
        return True