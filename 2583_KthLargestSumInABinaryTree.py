# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelSum = {}
        
        stack = deque([[root, 0]])
        while stack:
            node, depth = stack.popleft()
            levelSum[depth] = levelSum.get(depth, 0) + node.val
            if node.left:
                stack.append([node.left, depth + 1])
            if node.right:
                stack.append([node.right, depth + 1])
        
        nums = list(levelSum.values())
        return self.findKthLargest(nums, len(nums) + 1 - k)
        
    def findKthLargest(self, nums, k):
        if len(nums) < k or k <= 0:
            return -1
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        pivot = nums[0]
        start, end = 0, len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] > pivot:
                swap(i, end)
                end -= 1
            elif nums[i] < pivot:
                swap(i, start)
                start += 1
                i += 1
            else:
                i += 1
        if k > end + 1:
            return self.findKthLargest(nums[end+1:], k - (end + 1))
        elif k > start:
            return pivot
        else:
            return self.findKthLargest(nums[:start], k)
    