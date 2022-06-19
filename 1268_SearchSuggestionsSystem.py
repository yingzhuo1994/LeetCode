# 1st solution
from bisect import bisect


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

# 2nd solution
# O(N*log(N)) time | O(M) space
# where N is the lenth of products, and M is the length of searchWord.
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans, prefix, i = [], '', 0
        for ch in searchWord:
            prefix += ch
            i = bisect.bisect_left(products, prefix, i)
            ans.append([w for w in products[i:i+3] if w.startswith(prefix)])
        return ans