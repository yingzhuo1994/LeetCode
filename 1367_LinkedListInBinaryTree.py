# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        valDic = {}
        def dfs(node):
            if not node:
                return
            if node.val not in valDic:
                valDic[node.val] = []
            valDic[node.val].append(node)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        p = head
        if p.val not in valDic:
            return False
        nodes = valDic[p.val]

        p = p.next
        while p:
            level = []
            for node in nodes:
                if node.left and node.left.val == p.val:
                    level.append(node.left)
                if node.right and node.right.val == p.val:
                    level.append(node.right)
            nodes = level
            if not nodes:
                return False
            p = p.next
        return True

