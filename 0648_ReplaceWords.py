# 1st solution
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        trie = Trie()
        for word in dictionary:
            trie.add(word)
        for i in range(len(words)):
            words[i] = trie.find(words[i])
        
        return " ".join(words)

class Trie:
    def __init__(self):
        self.dic = {}
        self.end = "*"
    
    def add(self, word):
        dic = self.dic
        for ch in word:
            if ch not in dic:
                dic[ch] = {}
            dic = dic[ch]
        dic[self.end] = word
    
    def find(self, word):
        dic = self.dic
        for i, ch in enumerate(word):
            if ch in dic:
                dic = dic[ch]
            else:
                break
            if self.end in dic:
                return dic[self.end]
        return word