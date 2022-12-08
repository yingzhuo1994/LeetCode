# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(log(n)) space
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeaves(root1, []) == self.getLeaves(root2, [])

    def getLeaves(self, node, leaves):
        if not node:
            return leaves
        if node.left:
            self.getLeaves(node.left, leaves)
        if node.right:
            self.getLeaves(node.right, leaves)
        if not node.left and not node.right:
            leaves.append(node.val)
        return leaves

# 2nd solution
# O(n) time | O(log(n)) space
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack1, stack2 = deque([root1]), deque([root2])
        
        while stack1 and stack2:
            while stack1[-1].left or stack1[-1].right:
                node = stack1.pop()
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)
            v1 = stack1.pop().val

            while stack2[-1].left or stack2[-1].right:
                node = stack2.pop()
                if node.right:
                    stack2.append(node.right)
                if node.left:
                    stack2.append(node.left)
            v2 = stack2.pop().val
            if v1 != v2:
                return False
        return not stack1 and not stack2

# 3rd solution
# O(n) time | O(log(n)) space
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return
            if not node.left and not node.right: yield node.val
            for i in dfs(node.left): yield i
            for i in dfs(node.right): yield i
        return all(a == b for a, b in itertools.zip_longest(dfs(root1), dfs(root2)))