# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution, bfs
# O(n) time | O(n) space
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        level = [root]
        ans = []
        while level:
            curSum = 0
            newLevel = []
            for node in level:
                curSum += node.val
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            ans.append(float(curSum) / len(level))
            level = newLevel
        return ans

# 2nd solution, dfs
# O(n) time | O(h) space
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        level = [[root, 0]]
        levelSum = []
        levelCount = []
        while level:
            node, depth = level.pop()
            if depth >= len(levelSum):
                levelSum.append(node.val)
                levelCount.append(1)
            else:
                levelSum[depth] += node.val
                levelCount[depth] += 1
            if node.right:
                level.append([node.right, depth + 1])
            if node.left:
                level.append([node.left, depth + 1])
        return [float(value) / count for value, count in zip(levelSum, levelCount)]