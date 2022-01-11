# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution, recursive
# O(n) time | O(h) space
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root, 0)
        return self.ans
    
    def dfs(self, node, cur):
        if not node:
            return
         
        cur = (cur << 1) | node.val
        if not node.left and not node.right:
            self.ans += cur
            return 
        
        self.dfs(node.left, cur)
        self.dfs(node.right, cur)

# 2nd solution, iterative
# O(n) time | O(h) space
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [(root, 0)]
        while stack:
            node, cur = stack.pop()
            if node is not None:
                cur = (cur << 1) | node.val
                
                if node.left is None and node.right is None:
                    ans += cur
                else:
                    stack.append((node.right, cur))
                    stack.append((node.left, cur))
        return ans

# 3rd solution, Morris
# O(n) time | O(1) space
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        root_to_leaf = curr_number = 0
        
        while root:  
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left: 
                # Predecessor node is one step to the left 
                # and then to the right till you can.
                predecessor = root.left 
                steps = 1
                while predecessor.right and predecessor.right is not root: 
                    predecessor = predecessor.right 
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = (curr_number << 1) | root.val                    
                    predecessor.right = root  
                    root = root.left  
                # Break the link predecessor.right = root
                # Once the link is broken, 
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curr_number >>= 1
                    predecessor.right = None
                    root = root.right 
                    
            # If there is no left child
            # then just go right.        
            else: 
                curr_number = (curr_number << 1) | root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right
                        
        return root_to_leaf