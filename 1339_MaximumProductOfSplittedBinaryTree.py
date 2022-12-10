# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        memo = {}
        ans = 0
        def dfs(node):
            if not node:
                return 0
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            memo[node] = leftSum + rightSum + node.val
            return memo[node]
        dfs(root)

        def compare(node):
            nonlocal ans
            if not node:
                return 
            if node.left:
                leftSum = memo[node.left]
                rightSum = memo[root] - leftSum

                ans = max(ans, leftSum * rightSum)
                compare(node.left)
            if node.right:
                rightSum = memo[node.right]
                leftSum = memo[root] - rightSum
                ans = max(ans, leftSum * rightSum)
                compare(node.right)
        compare(root)
        return ans % MOD

# 2nd solution
# O(n) time | O(h) space
class Solution:
    def maxProduct(self, root):
        self.res = total = 0

        def dfs(root):
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            self.res = max(self.res, left * (total - left), right * (total - right))
            return left + right + root.val

        total = dfs(root)
        dfs(root)
        return self.res % (10**9 + 7)