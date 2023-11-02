# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dic = Counter()
        self.count = 0
        def dfs(node):
            if not node:
                return
            self.dic[node.val] += 1
            self.count = max(self.count, self.dic[node.val])
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        self.ans = []
        for k, v in self.dic.items():
            if v == self.count:
                self.ans.append(k)
        return self.ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.flag = False
        self.maxCount = 0
        self.curCount = 0
        self.curItem = None
        self.modeSize = 0

        self.inorder(root)
        self.rst = [-1] * self.modeSize
        self.flag = True
        self.curCount = 0
        self.modeSize = 0

        self.inorder(root)

        return self.rst

    def inorder(self, root):
        node = root
        while node:
            if not node.left: 
                self.handle(node.val)
                node = node.right
            else:
                pre = node.left
                while pre.right and pre.right != node: 
                    pre = pre.right
                
                if not pre.right: 
                    pre.right = node
                    node = node.left
                else: 
                    self.handle(node.val)
                    pre.right = None
                    node = node.right

    def handle(self, v):
        if v != self.curItem: 
            self.curItem = v
            self.curCount = 0
        self.curCount += 1
        
        if self.curCount > self.maxCount:
            self.modeSize = 1
            self.maxCount = self.curCount
        elif self.curCount == self.maxCount:
            if self.flag: 
                self.rst[self.modeSize] = v
            self.modeSize += 1