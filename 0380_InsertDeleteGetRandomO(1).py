class RandomizedSet:

    # 1st solution
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack, self.pos = [], {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.stack.append(val)
            self.pos[val] = len(self.stack) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            idx, last = self.pos[val], self.stack[-1]
            self.stack[idx], self.pos[last] = last, idx
            self.stack.pop()
            self.pos.pop(val, 0)
            return True
        return False
    
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.stack)


    # 2nd solution
    # O(1) time | O(n) space
    def __init__(self):
        self.dic_direct = {}
        self.dic_invert = {}
        self.num_elem = 0
        
    def insert(self, val: int) -> bool:
        if val in self.dic_invert:
            return False
        else:
            self.dic_invert[val] = self.num_elem
            self.dic_direct[self.num_elem] = val
            self.num_elem += 1
            return True
        
    def remove(self, val):
        if val not in self.dic_invert:
            return False
        else:
            idx = self.dic_invert.pop(val)
            self.dic_direct.pop(idx)
            if idx != self.num_elem - 1:
                self.dic_direct[idx] = self.dic_direct[self.num_elem - 1]
                self.dic_invert[self.dic_direct[self.num_elem - 1]] = idx
                self.dic_direct.pop(self.num_elem - 1)
            self.num_elem -= 1
            return True
        
    def getRandom(self):
        index = floor(random.random()*self.num_elem)
        return self.dic_direct[index]