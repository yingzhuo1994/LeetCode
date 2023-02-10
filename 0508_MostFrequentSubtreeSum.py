# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.dic = Counter()
        def dfs(node):
            if not node:
                return 0
            val = node.val
            leftVal = dfs(node.left)
            rightVal = dfs(node.right)
            curSum = val + leftVal + rightVal
            self.dic[curSum] += 1
            return curSum
        dfs(root)
        maxFreq = max(self.dic.values())
        ans = []
        for val in self.dic:
            if self.dic[val] == maxFreq:
                ans.append(val)
        return ans
