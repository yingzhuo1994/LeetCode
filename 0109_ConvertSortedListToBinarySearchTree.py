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
# O(n^2) time | O(log(n)) space
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        if length == 0:
            return None
        elif length == 1:
            return TreeNode(head.val)
        halfLength = length // 2
        prev = None
        node = head
        for i in range(halfLength):
            prev = node
            node = node.next
        prev.next = None
        root = TreeNode(node.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(node.next)
        return root

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        lst = []
        node = head
        while node:
            lst.append(node.val)
            node = node.next
        return self.dfs(lst, 0, len(lst) - 1)

    def dfs(self, lst, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        root = TreeNode(lst[mid])
        root.left = self.dfs(lst, start, mid - 1)
        root.right = self.dfs(lst, mid + 1, end)
        return root

# 3rd solution
# O(n) time | O(log(n)) space
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        length = 0
        node = head
        self.head = head
        while node:
            node = node.next
            length += 1
        return self.dfs(0, length - 1)

    def dfs(self, left, right):
        if left > right: return None
        mid = (left + right) // 2
        leftNode = self.dfs(left, mid - 1)
        
        root = TreeNode(self.head.val)
        self.head = self.head.next
        
        root.left = leftNode
        root.right = self.dfs(mid + 1, right)
        return root