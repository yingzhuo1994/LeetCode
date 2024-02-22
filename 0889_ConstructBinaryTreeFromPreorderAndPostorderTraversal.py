# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        leftLength = postorder.index(preorder[1]) + 1
        root.left = self.constructFromPrePost(preorder[1:1+leftLength], postorder[:leftLength])
        root.right = self.constructFromPrePost(preorder[1+leftLength:], postorder[leftLength:-1])
        return root

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = {x: i for i, x in enumerate(postorder)}

        def dfs(pre_l: int, pre_r: int, post_l: int, post_r: int) -> Optional[TreeNode]:
            if pre_l == pre_r:  # 空节点
                return None
            if pre_l + 1 == pre_r:  # 叶子节点
                return TreeNode(preorder[pre_l])
            left_size = index[preorder[pre_l + 1]] - post_l + 1  # 左子树的大小
            left = dfs(pre_l + 1, pre_l + 1 + left_size, post_l, post_l + left_size)
            right = dfs(pre_l + 1 + left_size, pre_r, post_l + left_size, post_r - 1)
            return TreeNode(preorder[pre_l], left, right)

        return dfs(0, len(preorder), 0, len(postorder))  # 左闭右开区间