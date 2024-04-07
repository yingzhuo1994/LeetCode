# 1st solution
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.parents = {kingName: None}
        self.children = {kingName: []}
        self.states = {self.kingName: True}
        self.childIdx = {self.kingName: 0}
        
    def birth(self, parentName: str, childName: str) -> None:
        self.parents[childName] = parentName
        self.childIdx[childName] = len(self.children[parentName])
        self.children[parentName].append(childName)
        self.children[childName] = []
        self.states[childName] = True

    def death(self, name: str) -> None:
        self.states[name] = False
        if name == self.kingName:
            self.kingName = self.getSuccessor(name, 0)
            
    def getInheritanceOrder(self) -> List[str]:
        name = self.kingName
        lst = []
        while name:
            lst.append(name)
            name = self.getSuccessor(name, 0)
        return lst
        
    def getSuccessor(self, name, idx):
        for i in range(idx, len(self.children[name])):
            child = self.children[name][i]
            if self.states[child]:
                return child
            else:
                child = self.getSuccessor(child, 0)
                if child:
                    return child
        if self.parents[name]:
            return self.getSuccessor(self.parents[name], self.childIdx[name] + 1)
        return None
        
        



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()