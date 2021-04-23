# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # O(n) time | O(1) space
        sentinel = ListNode(0, head)
        p = sentinel.next
        length = 0
        while p:
            length += 1
            p = p.next
        p = sentinel
        k = 0
        while k < length - n:
            p = p.next
            k += 1
        p.next = p.next.next
        return sentinel.next
