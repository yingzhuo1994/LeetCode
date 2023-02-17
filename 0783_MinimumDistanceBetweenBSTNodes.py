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

# 2nd solution
# O(n) time | O(h) space
# where n is number of nodes and h is the height of the tree
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans = float("inf")
        self.lastVal = float("-inf")

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            diff = node.val - self.lastVal
            self.ans = min(self.ans, diff)
            self.lastVal = node.val
            dfs(node.right)

        dfs(root)
        return self.ans

# 3rd solution, Morris Traversal
# O(n) time | O(1) space
# where n is number of nodes
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans = float("inf")
        self.lastVal = float("-inf")

        def dfs(node):
            while node:
                if not node.left:
                    diff = node.val - self.lastVal
                    self.ans = min(self.ans, diff)
                    self.lastVal = node.val
                    node = node.right
                else:
                    curNode = node.left
                    while curNode.right and curNode.right != node:
                        curNode = curNode.right
                    
                    if curNode.right != node:
                        curNode.right = node
                        node = node.left
                    else:
                        diff = node.val - self.lastVal
                        self.ans = min(self.ans, diff)
                        self.lastVal = node.val
                        curNode.right = None
                        node = node.right

        dfs(root)
        return self.ans