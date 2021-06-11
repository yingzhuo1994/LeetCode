# 1st solution
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.stack.append(word)
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.stack:
            return True
        return False
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        n = len(prefix)
        for word in self.stack:
            if len(word) >= n and prefix == word[:n]:
                return True
        return False
        
# 2nd solution
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = {}
        self.endMark = '*'
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.stack
        for i in range(len(word)):
            ch = word[i]
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self.endMark] = True    
        # print(self.stack)
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.stack
        for i in range(len(word)):
            ch = word[i]
            if ch in node:
                node = node[ch]
            else:
                return False
        return self.endMark in node
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.stack
        for i in range(len(prefix)):
            ch = prefix[i]
            if ch in node:
                node = node[ch]
            else:
                return False
        return True    
    