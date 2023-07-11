# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1st solution
# O(n) time | O(n) space
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent=None):
            if not node:
                return
            parents[node.val] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        def search(node, prev, distance):
            if not node:
                return
            if distance == 0:
                self.ans.append(node.val)
                return
            neig = [node.left, node.right, parents[node.val]]
            for nextNode in neig:
                if nextNode == prev:
                    continue
                search(nextNode, node, distance - 1)
        parents = {}
        self.ans = []
        dfs(root)
        search(target, None, k)

        return self.ans
