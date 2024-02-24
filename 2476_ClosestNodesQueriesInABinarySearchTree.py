# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n * log(m)) time | O(n + h) space
# where m is the number of nodes, h is the tree height
# n = len(queries)
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def queryMin(node, val):
            if not node:
                return -1
            
            if node.val > val:
                return queryMin(node.left, val)
            elif node.val < val:
                return max(node.val, queryMin(node.right, val))
            else:
                return val
            
        
        def queryMax(node, val):
            if not node:
                return float("inf")
            
            if node.val > val:
                return min(node.val, queryMax(node.left, val))
            elif node.val < val:
                return queryMax(node.right, val)
            else:
                return val
        
        ans = [[queryMin(root, val), queryMax(root, val)] for val in queries]
        for i in range(len(ans)):
            if ans[i][1] == float("inf"):
                ans[i][1] = -1
        return ans

# 2nd solution
# O(n + qlog(n)) time | O(n) space
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        array = []
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)
            array.append(node.val)
            dfs(node.right)
        dfs(root)

        n = len(array)
        ans = []
        for q in queries:
            j = bisect_left(array, q)
            mx = array[j] if j < n else -1
            if j == n or array[j] != q:  # a[j]>q, a[j-1]<q
                j -= 1
            mn = array[j] if j >= 0 else -1
            ans.append([mn, mx])
        return ans
