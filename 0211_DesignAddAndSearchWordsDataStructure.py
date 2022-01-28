class WordDictionary:

    def __init__(self):
        self.dic = {}
        self.end = "*"
        
    def addWord(self, word: str) -> None:
        dic = self.dic
        for ch in word:
            if ch not in dic:
                dic[ch] = {}
            dic = dic[ch]
        dic[self.end] = True
        # print(self.dic)
 
    def search(self, word: str) -> bool:
        stack = [self.dic]
        for ch in word:
            newStack = []
            if ch == ".":
                for dic in stack:
                    for k in dic.keys():
                        if k != self.end:
                            newStack.append(dic[k])
            else:
                for dic in stack:
                    if ch in dic:
                        newStack.append(dic[ch])
            if len(newStack) == 0:
                return False
            stack = newStack
        for dic in stack:
            if self.end in dic:
                return True
        return False
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)