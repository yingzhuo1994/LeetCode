# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1st solution
    # O(n) time | O(n^2) space
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        val = preorder[0]
        node = TreeNode(val)
        breakIndex = 0
        for i in range(1, len(preorder)):
            if preorder[i] < val:
                breakIndex = i
            else:
                break
        node.left = self.bstFromPreorder(preorder[1:breakIndex + 1])
        node.right = self.bstFromPreorder(preorder[breakIndex + 1:])
        return node

    # 2nd solution
    # O(n) time | O(n) space
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(down, up):
            if self.idx >= len(preorder): return None
            if not down < preorder[self.idx] < up: return None
            root = TreeNode(preorder[self.idx])
            self.idx += 1
            root.left = helper(down, root.val)
            root.right = helper(root.val, up)
            return root
        
        self.idx = 0
        return helper(-float("inf"), float("inf"))