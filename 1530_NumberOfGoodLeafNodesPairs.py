# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O((h^3) + n) time | O(h) space
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return {}
            if not node.left and not node.right:
                return {0: 1}
            leftDic = dfs(node.left)
            rightDic = dfs(node.right)
            for a in leftDic:
                for b in rightDic:
                    if a + b + 2 <= distance:
                        self.ans += leftDic[a] * rightDic[b]
            dic = {}
            for a in leftDic:
                dic[a + 1] = leftDic[a]
            for b in rightDic:
                dic[b + 1] = dic.get(b + 1, 0) + rightDic[b]
            
            return dic
        dfs(root)
        return self.ans