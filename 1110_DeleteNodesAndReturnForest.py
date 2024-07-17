# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(n) space
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        parents = {}
        nodes = {}
        def dfs(node, parent):
            if node:
                parents[node.val] = parent
                nodes[node.val] = node
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root, None)
        deleteSet = set(to_delete)
        ans = []
        if root and root.val not in deleteSet:
            ans.append(root)

        for val in to_delete:
            if val not in nodes:
                continue
            node = nodes[val]
            if node.left and node.left.val not in deleteSet:
                ans.append(node.left)
            if node.right and node.right.val not in deleteSet:
                ans.append(node.right)
            parent = parents[node.val]
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
        return ans