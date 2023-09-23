class LockingTree:

    def __init__(self, parent: List[int]):
        self.parents = {i: p for i, p in enumerate(parent)}
        self.children = [[] for _ in range(len(parent))]
        for child in self.parents:
            p = self.parents[child]
            if p == -1:
                continue
            self.children[p].append(child)

        self.dic = {i: None for i in range(len(parent))}

    def lock(self, num: int, user: int) -> bool:
        if self.dic[num] is None:
            self.dic[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.dic[num] == user:
            self.dic[num] = None
            return True
        return False
        
    def upgrade(self, num: int, user: int) -> bool:
        if self.dic[num] is not None:
            return False
        if not self.hasLockedChild(num):
            return False
        if self.hasLockedParent(num):
            return False
        self.dic[num] = user
        self.unlockChildren(num)
        return True
    
    def hasLockedChild(self, num):
        for child in self.children[num]:
            if self.dic[child] is not None:
                return True
            if self.hasLockedChild(child):
                return True
        return False
    
    def hasLockedParent(self, num):
        p = self.parents[num]
        if p == -1:
            return False
        if self.dic[p] is not None:
            return True
        return self.hasLockedParent(p)
    
    def unlockChildren(self, num):
        for child in self.children[num]:
            self.dic[child] = None
            self.unlockChildren(child)
        

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)