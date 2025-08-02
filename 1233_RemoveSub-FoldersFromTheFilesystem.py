# 1st solution
# O(n) time | O(n) space
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for dir in folder:
            trie.add(dir)
        return trie.getFolder()
        


class Trie:
    def __init__(self):
        self.root = {}
        self.end = "*"
    
    def add(self, dir):
        lst = dir.split("/")
        dic = self.root
        for i in range(1, len(lst)):
            if self.end in dic:
                return
            folder = lst[i]
            if folder not in dic:
                dic[folder] = {}
            dic = dic[folder]
        dic[self.end] = True
    
    def getFolder(self, dic=None):
        if dic is None:
            dic = self.root
        ans = []
        if self.end in dic:
            return [""]
        for dir in dic:
            lst = self.getFolder(dic[dir])
            ans += ["/" + dir + d for d in lst]
        return ans
