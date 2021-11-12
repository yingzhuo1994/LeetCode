# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1st solution
# O(n) time | O(n) space
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(0)
        p = sentinel
        while head:
            if head.val != val:
                p.next = ListNode(head.val)
                p = p.next
            head = head.next
        return sentinel.next

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode(0)
        p = sentinel
        while head:
            if head.val != val:
                p.next = head
                p = p.next
            temp = head
            head = head.next
            temp.next = None
        return sentinel.next