# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(logn) space
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        p = TreeNode(nums[mid])
        p.left = self.sortedArrayToBST(nums[:mid])
        p.right = self.sortedArrayToBST(nums[mid+1:])
        return p

# 2nd solution
# O(n) time | O(logn) space
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(start, end):
            if start > end:
                return None

            mid = start + (end - start) // 2
            root = TreeNode(nums[mid])
            root.left = helper(start, mid - 1)
            root.right = helper(mid + 1, end)
            
            return root
        return helper(0, len(nums) - 1)