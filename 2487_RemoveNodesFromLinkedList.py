# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(n) space
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = [head]
        node = head.next
        while node:
            while stack and stack[-1].val < node.val:
                old = stack.pop()
            if stack:
                stack[-1].next = node
            stack.append(node)
            node = node.next
        stack[-1].next = None
        return stack[0]
            