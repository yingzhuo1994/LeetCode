# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution, DFS
# O(n) time | O(h) space
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sumDic = {}
        def dfs(node, depth):
            if not node:
                return
            sumDic[depth] = sumDic.get(depth, 0) + node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        def dfs_replace(node, depth):
            if not node:
                return
            value = 0
            if node.left:
                value += node.left.val
            if node.right:
                value += node.right.val
            
            newValue = sumDic.get(depth + 1, 0) - value
            if node.left:
                node.left.val = newValue
            if node.right:
                node.right.val = newValue
            
            dfs_replace(node.left, depth + 1)
            dfs_replace(node.right, depth + 1)
        
        dfs(root, 0)
        dfs_replace(root, 0)
        root.val = 0
        return root

# 2nd solution, BFS
# O(n) time | O(n) space
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        level = [root]
        while level:
            newLevel = []

            # 计算下一层的节点值之和
            next_level_sum = 0
            for node in level:
                if node.left:
                    newLevel.append(node.left)
                    next_level_sum += node.left.val
                if node.right:
                    newLevel.append(node.right)
                    next_level_sum += node.right.val

            # 再次遍历，更新下一层的节点值
            for node in level:
                children_sum = (node.left.val if node.left else 0) + \
                               (node.right.val if node.right else 0)
                if node.left:
                    node.left.val = next_level_sum - children_sum
                if node.right:
                    node.right.val = next_level_sum - children_sum
            
            level = newLevel
        return root