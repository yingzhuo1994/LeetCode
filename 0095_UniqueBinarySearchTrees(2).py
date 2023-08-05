# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O((2n)!/((n+1)! * n!)) time | O((2n)!/((n+1)! * n!))
# Catalan number
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = defaultdict(list)
        def buildTree(start, end):
            if start > end:
                return [None]
            if (start, end) not in memo:
                ans = []
                if start == end:
                    ans.append(TreeNode(start))
                else:
                    for i in range(start, end + 1):
                        leftNodes = buildTree(start, i - 1)
                        rightNodes = buildTree(i + 1, end)
                        for leftNode in leftNodes:
                            for rightNode in rightNodes:
                                node = TreeNode(i)
                                node.left = leftNode
                                node.right = rightNode
                                ans.append(node)
                memo[(start, end)] = ans
            return memo[(start, end)]
        return buildTree(1, n)

# 2nd solution