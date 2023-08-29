# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def buildTree(start, end):
            if start > end:
                return None
            elif start == end:
                return TreeNode(nums[start])
            
            idx, maxVal = start, nums[start]
            for i in range(start, end + 1):
                if nums[i] > maxVal:
                    idx = i
                    maxVal = nums[i]
            
            root = TreeNode(maxVal)
            root.left = buildTree(start, idx - 1)
            root.right = buildTree(idx + 1, end)
            
            return root
        
        return buildTree(0, len(nums) - 1)

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []

        for num in nums:
            node = TreeNode(num)
            while stack and num > stack[-1].val:
                node.left = stack.pop()

            if stack:
                stack[-1].right = node               
            stack.append(node)

        return stack[0]