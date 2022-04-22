# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution, Morris Traversal
# O(n) time | O(1) space
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curNode, lastNode = root, TreeNode(-float("inf"))
        candidates = []
        while curNode:
            if not curNode.left:
                if curNode.val < lastNode.val:
                    candidates += [lastNode, curNode]
                lastNode = curNode
                curNode = curNode.right
            else:
                pre = curNode.left
                while pre.right and pre.right != curNode:
                    pre = pre.right
                if not pre.right:
                    pre.right = curNode
                    curNode = curNode.left
                else:
                    pre.right = None
                    if curNode.val < lastNode.val:
                        candidates += [lastNode, curNode]
                    lastNode = curNode
                    curNode = curNode.right

        self.swap(candidates[0], candidates[-1])
    
    def swap(self, node1, node2):
        node1.val, node2.val = node2.val, node1.val