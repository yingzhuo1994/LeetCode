# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n^2) time | O(log(n)) space
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        stack = [root]
        count = 0
        while stack:
            curNode = stack.pop()
            if curNode:
                count += self.pathSumHelper(curNode, targetSum)
                stack.append(curNode.left)
                stack.append(curNode.right)
        return count

    def pathSumHelper(self, node, targetSum):
        if not node:
            return 0
        count = 0
        if node.val == targetSum:
            count += 1
        count += self.pathSumHelper(node.left, targetSum - node.val)
        count += self.pathSumHelper(node.right, targetSum - node.val)
        return count

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        cache = {0:1}

        self.dfs(root, targetSum, 0, cache)

        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        if root is None:
            return
        
        currPathSum += root.val
        oldPathSum = currPathSum - target
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)

        cache[currPathSum] -= 1