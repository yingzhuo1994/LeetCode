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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = self.reverseList(head)
        while cur.next:
            if cur.val > cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return self.reverseList(head)