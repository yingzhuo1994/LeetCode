# 1st solution
class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.trie = Trie()
        self.addWords(words)
        
        
    def f(self, prefix: str, suffix: str) -> int:
        trie = self.trie
        prefixIdx = trie.searchPrefix(prefix)
        suffixIdx = trie.searchSuffix(suffix)
        ans = -1
        for idx in prefixIdx:
            if idx in suffixIdx and idx > ans:
                ans = idx
        return ans
    
    def addWords(self, words):
        wordDic = {}
        for idx, word in enumerate(words):
            wordDic[word] = idx
        
        for word, idx in wordDic.items():
            self.trie.addPrefix(word, idx)
            self.trie.addSuffix(word, idx)
            
class Trie:
    def __init__(self):
        self.prefix = {}
        self.suffix = {}
        self.end = "*"
    
    def addPrefix(self, word, idx):
        dic = self.prefix
        for ch in word:
            if ch not in dic:
                dic[ch] = {self.end: set()}
            dic[ch][self.end].add(idx)
            dic = dic[ch]
    
    def addSuffix(self, word, idx):
        dic = self.suffix
        for i in reversed(range(len(word))):
            ch = word[i]
            if ch not in dic:
                dic[ch] = {self.end: set()}
            dic[ch][self.end].add(idx)
            dic = dic[ch]

    def searchPrefix(self, prefix):
        dic = self.prefix
        for ch in prefix:
            if ch not in dic:
                return set()
            dic = dic[ch]

        return dic[self.end]

    def searchSuffix(self, suffix):
        dic = self.suffix
        for i in reversed(range(len(suffix))):
            ch = suffix[i]
            if ch not in dic:
                return set()
            dic = dic[ch]

        return dic[self.end]
        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)