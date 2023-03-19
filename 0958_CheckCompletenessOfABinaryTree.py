# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def getDepth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth
        
        if not root.left:
            return not root.right
        depth = getDepth(root)
        level = [root]
        i = 1
        while i < depth - 1:
            newLevel = []
            for node in level:
                if not node.left or not node.right:
                    return False
                newLevel.append(node.left)
                newLevel.append(node.right)
            level = newLevel
            i += 1
        
        hasToBeNone = False
        newLevel = []
        for node in level:
            if hasToBeNone:
                if node.left or node.right:
                    return False
            else:
                if node.left:
                    newLevel.append(node.left)
                    if node.right:
                        newLevel.append(node.right)
                    else:
                        hasToBeNone = True
                else:
                    hasToBeNone = True
                    if node.right:
                        return False
        for node in newLevel:
            if node.left or node.right:
                return False
        return True

# 2nd solution, bfs
# O(n) time | O(n) space
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])
    
# 3rd solution, dfs
# O(n) time | O(n) space
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: 
                return 0
            l, r = dfs(node.left), dfs(node.right)
            if l & (l + 1) == 0 and l // 2 <= r <= l:
                return l + r + 1
            if r & (r + 1) == 0 and r <= l <= r * 2 + 1:
                return l + r + 1
            return -1
        return dfs(root) > 0