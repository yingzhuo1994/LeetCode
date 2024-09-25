# 1st solution
# O(nk) time | O(nk) space
# where n = len(words) and k is largest length of word in words
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add(word)
        return [trie.get_score(word) for word in words]
    

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
            dic[self.end] = dic.get(self.end, 0) + 1
    
    def get_score(self, word):
        dic = self.root
        score = 0
        for ch in word:
            dic = dic[ch]
            score += dic.get(self.end, 0)
        return score