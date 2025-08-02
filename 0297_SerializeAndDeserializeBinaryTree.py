# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1st solution
# O(n) time | O(n) space
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        # there should be a whitespace between each number
        return ' '.join(vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()       

# 2nd solution
# O(n) time | O(n) space
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        
        children = [root.left, root.right] # for binary tree

        data = str(root.val) + ',' + str(len(children))
        for child in children:
            data += ',' + self.serialize(child)
        return data
        
    
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        datalist = collections.deque(data.split(','))
        return self.solve(datalist)

    def solve(self, datalist):
        val = datalist.popleft()
        if val == '#':
            return None
        root = TreeNode(int(val))
        # root.children = []

        size = int(datalist.popleft())
        # for _ in range(size):
        #     root.children.append(self.solve(datalist))
        root.left = self.solve(datalist)
        root.right = self.solve(datalist)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))