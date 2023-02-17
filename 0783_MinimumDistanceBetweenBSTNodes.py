# 1st solution
# O(n * log(n)) time | O(n) space
# where n is number of nodes
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.values = set()
        self.ans = float("inf")
        def dfs(node):
            if not node:
                return
            if self.ans == 0:
                return 
            if node.val in self.values:
                self.ans = 0
                return
            self.values.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        if self.ans == 0:
            return self.ans
        values = sorted(list(self.values))
        for i in range(len(values) - 1):
            diff = values[i + 1]  - values[i]
            self.ans = min(self.ans, diff)
        return self.ans