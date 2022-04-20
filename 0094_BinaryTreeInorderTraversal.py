# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st recursive solution
# O(n) time | O(log(n)) space
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        leftTree = self.inorderTraversal(root.left)
        rightTree = self.inorderTraversal(root.right)
        return leftTree + [root.val] + rightTree

# 2nd Iterative solution
# O(n) time | O(n) space
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

# 3rd Morris Traversal
# O(n) time | O(1) space
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        curNode = root
        while curNode is not None:
            if curNode.left is None:
                ans.append(curNode.val)
                curNode = curNode.right
            else:
                # Find the inorder 
                # predecessor of current
                pre = curNode.left
                while pre.right is not None and pre.right is not curNode:
                    pre = pre.right

                if pre.right is None:
                    # Make current as right 
                    # child of its inorder predecessor
                    pre.right = curNode
                    curNode = curNode.left
                else:
                    # Revert the changes made 
                    # in the 'if' part to restore the
                    # original tree. i.e., fix
                    # the right child of predecessor
                    pre.right = None
                    ans.append(curNode.val)
                    curNode = curNode.right
        return ans