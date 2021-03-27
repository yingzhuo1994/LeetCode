# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        mid = n // 2
        L, R = mid - 1, mid + 1
        head = TreeNode(nums[mid])
        if n == 1:
            return head
        p = head
        if L >= 0:
            p.left = self.sortedArrayToBST(nums[:L+1])
        if R <= n - 1:
            p.right = self.sortedArrayToBST(nums[R:])
        return head
