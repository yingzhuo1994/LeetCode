# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.length = self.get_length(self.root)
    
    def get_length(self, node):
        if not node:
            return 0
        return 1 + self.get_length(node.left) + self.get_length(node.right)

    def insert(self, val: int) -> int:
        self.length += 1
        k = self.length
        position = []
        while k > 0:
            if k & 1:
                position.append(1)
            else:
                position.append(0)
            k >>= 1
        position.reverse()
        # print(self.length, position)
        node = self.get_root()
        for i in range(1, len(position) - 1):
            if position[i]:
                node = node.right
            else:
                node = node.left
        newNode = TreeNode(val)
        if position[-1]:
            node.right = newNode
        else:
            node.left = newNode
        return node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()