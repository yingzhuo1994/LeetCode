# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        parents = {}
        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            parents[child] = parent
            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        for node in nodes:
            if node not in parents:
                return nodes[node]
        return None
        