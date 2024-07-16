# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parents = {}
        nodes = {}
        def dfs(node, parent):
            parents[node.val] = parent
            nodes[node.val] = node
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)
        dfs(root, None)
        level = deque([[startValue, ""]])
        visited = set([startValue])
        while level:
            val, path = level.popleft()
            node = nodes[val]
            parent = parents[val]
            if node.val == destValue:
                return path
            if node.left and node.left.val not in visited:
                visited.add(node.left.val)
                level.append([node.left.val, path + "L"])
            if node.right and node.right.val not in visited:
                visited.add(node.right.val)
                level.append([node.right.val, path + "R"])
            if parent and parent.val not in visited:
                visited.add(parent.val)
                level.append([parent.val, path + "U"])
        return ""