# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.recover(self.root, 0)
        

    def find(self, target: int) -> bool:
        path = [target]
        val = target
        while val > 0:
            if val & 1:
                val = (val - 1) // 2
            else:
                val = (val - 2) // 2
            path.append(val)
        node = self.root
        for i in reversed(range(len(path))):
            val = path[i]
            if not node or node.val != val:
                return False
            if i > 0:
                if path[i-1] & 1:
                    node = node.left
                else:
                    node = node.right
        return True
    

    def recover(self, node, val):
        if not node:
            return
        node.val = val
        self.recover(node.left, val * 2 + 1)
        self.recover(node.right, val * 2 + 2)


# 2nd solution
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.recover(self.root, 0)
        

    def find(self, target: int) -> bool:
        binary = bin(target+1)[3:]                  # remove the useless first `1`
        index = 0
        root = self.root                                    # use a new pointer `root` to traverse the tree
        while root and index <= len(binary): # traverse the binary number from left to right
            if root.val == target:
                return True
            if  binary[index] == '0':  # if it's 0, we have to go left
                root = root.left
            else:  # if it's 1, we have to go right
                root = root.right
            index += 1
        return False
    

    def recover(self, node, val):
        if not node:
            return
        node.val = val
        self.recover(node.left, val * 2 + 1)
        self.recover(node.right, val * 2 + 2)

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)