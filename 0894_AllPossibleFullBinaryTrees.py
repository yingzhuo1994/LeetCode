# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(2^(n/2)) time | O(n * 2^(n/2)) space
class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode(0)]

        ans = []
        for i in range(1, n - 1, 2):
            leftNodes = self.allPossibleFBT(i)
            rightNodes = self.allPossibleFBT(n - 1 - i)
            for left in leftNodes:
                for right in rightNodes:
                    root = TreeNode()
                    root.left = left
                    root.right = right
                    ans.append(root)
        
        return ans
