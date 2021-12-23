# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(1) space
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = self.reverseList(slow)
        first = head
        sentinel = ListNode(0)
        p = sentinel
        while first != slow:
            p.next = first
            first = first.next
            p = p.next
            p.next = second
            second = second.next
            p = p.next
        return sentinel.next

    def reverseList(self, head):
        prev = None
        while head:
            node = head.next
            head.next = prev
            prev = head
            head = node
        return prev
