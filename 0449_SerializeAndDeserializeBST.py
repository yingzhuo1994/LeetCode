# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1st solution
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return "*"
        stack = [str(root.val)]
        left = self.serialize(root.left)
        stack.append("#")
        stack.append(left)
        right = self.serialize(root.right)
        stack.append("#")
        stack.append(right)
        ans = "".join(stack)
        return ans

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        idx = 0
        def search():
            nonlocal idx
            if idx == len(data):
                return None
            if data[idx] == "*":
                idx += 2
                return None
            start = idx
            while data[idx] != "#":
                idx += 1
            s = data[start:idx]
            value = int(s)
            root = TreeNode(value)
            idx += 1
            root.left = search()
            root.right = search()
            return root

        return search()
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans