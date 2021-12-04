class StreamChecker:

    def __init__(self, words: List[str]):
        self.dic = collections.defaultdict(dict)
        self.end = "*"
        self.formTrie(words)
        self.length = self.getTheLongestLengh(words)
        self.queryList = collections.deque()

    def query(self, letter: str) -> bool:
        self.queryList.appendleft(letter)
        if len(self.queryList) > self.length:
            self.queryList.pop()
        dic = self.dic
        for ch in self.queryList:
            if ch in dic:
                dic = dic[ch]
                if self.end in dic:
                    return True
            else:
                return False
        return False
    
    def formTrie(self, words):
        for word in words:
            self.addWord(word[::-1])

    def addWord(self, word):
        dic = self.dic
        for ch in word:
            dic = dic.setdefault(ch, {})
        dic[self.end] = True
    
    def getTheLongestLengh(self, words):
        length = 0
        for word in words:
            length = max(length, len(word))
        return length

        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)