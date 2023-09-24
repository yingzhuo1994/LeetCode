class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.add(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.query(prefix)
        

class Trie:
    def __init__(self):
        self.root = Node()
        self.end = "*"
    
    def add(self, word, val):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]

        diff = val - node.val
        node.val = val

        if diff != 0:
            self.update(word, diff)
    
    def update(self, word, diff):
        node = self.root
        for ch in word:
            node = node.children[ch]
            node.total += diff
    
    def query(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.total

class Node:
    def __init__(self, val=0):
        self.val = val
        self.total = val
        self.children = {}
    
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)