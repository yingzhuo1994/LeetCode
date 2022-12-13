class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.size = 0
        self.dic = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        ans = True
        if val not in self.dic:
            self.dic[val] = set()
        else:
            ans = False

        self.stack.append(val)
        self.dic[val].add(self.size)
        self.size += 1
        return ans

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.dic:
            idx = self.dic[val].pop()
            if len(self.dic[val]) == 0:
                self.dic.pop(val)
            if idx != self.size - 1:
                self.stack[idx], self.stack[self.size-1] = self.stack[self.size-1], self.stack[idx]
                target = self.stack[idx]
                self.dic[target].remove(self.size - 1)
                self.dic[target].add(idx)
            self.stack.pop()
            self.size -= 1 
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.stack)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()