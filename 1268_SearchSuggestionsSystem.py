# 1st solution
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for product in products:
            trie.add(product)
        
        return trie.search(searchWord)

class Trie:
    def __init__(self):
        self.root = {}
        self.end = '*'
    
    def add(self, word):
        dic = self.root
        for ch in word:
            if ch not in dic:
                dic[ch] = {self.end: []}
            dic = dic[ch]
            dic[self.end].append(word)
    
    def search(self, word):
        ans = []
        dic = self.root
        for i, ch in enumerate(word):
            if ch not in dic:
                ans.extend([[] for _ in range(i, len(word))])
                break
            else:
                dic = dic[ch]
                lst = dic[self.end]
                length = min(3, len(lst))
                ans.append(lst[:length])
        return ans
