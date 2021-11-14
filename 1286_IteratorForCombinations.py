class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.string = characters
        self.combinationLength = combinationLength
        self.indexList = [i for i in range(combinationLength)]
        
    def next(self) -> str:
        if self.hasNext():
            result = []
            for idx in self.indexList:
                result.append(self.string[idx])
            return "".join(result)

    def hasNext(self) -> bool:
    
    def moveIndex(self):
        carry = 1
        for i in reversed(range(self.combinationLength)):
            curCount = self.indexList[i] + carry
            carry = curCount // self.combinationLength
            if carry > 0:
                self.indexList[i] = self.indexList[i]
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()