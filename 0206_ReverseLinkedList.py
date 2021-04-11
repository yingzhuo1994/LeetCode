# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = ListNode(0)
        p.next = ListNode(0)
        while head:
            p.next.val = head.val
            temp = ListNode(0)
            temp.next = p
            p = temp
            head = head.next
        return p.next.next
