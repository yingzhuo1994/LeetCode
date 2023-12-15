# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1st solution, bfs
# O(n) time | O(n) space
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        depth = 0
        while stack:
            newStack = []
            for node in stack:
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
            if depth % 2 == 0:
                left, right = 0, len(newStack) - 1
                while left < right:
                    newStack[left].val, newStack[right].val = newStack[right].val, newStack[left].val
                    left += 1
                    right -= 1
            stack = newStack
            depth += 1

        return root

# 2nd solution， dfs
# O(n) time | O(h) space
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode], is_odd_level: bool) -> None:
            if node1 is None: return
            if is_odd_level: node1.val, node2.val = node2.val, node1.val
            dfs(node1.left, node2.right, not is_odd_level)
            dfs(node1.right, node2.left, not is_odd_level)
        dfs(root.left, root.right, True)
        return root
