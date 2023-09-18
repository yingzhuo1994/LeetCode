class MagicDictionary:
    def __init__(self):
        self.dic = {}
        self.end = "***"

    def add(self, word):
        dic = self.dic
        for ch in word:
            if ch not in dic:
                dic[ch] = {}
            dic = dic[ch]
        dic[self.end] = True

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.add(word)

    def search(self, searchWord: str) -> bool:
        return self.checkWord(self.dic, searchWord, 0, False)
    

    def checkWord(self, dic, word, idx, changed):
        if changed:
            if idx == len(word):
                return self.end in dic
            if word[idx] not in dic:
                return False
            return self.checkWord(dic[word[idx]], word, idx + 1, changed)
        else:
            if idx == len(word):
                return False

            for ch in dic:
                if ch == self.end:
                    continue
                if ch == word[idx]:
                    if self.checkWord(dic[ch], word, idx + 1, changed):
                        return True
                    continue
                if self.checkWord(dic[ch], word, idx + 1, True):
                    return True
            return False




# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)