# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1st solution
    # O(n) time | O(1) space
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    # 2nd solution
    # O(n) time | O(1) space
    def reverseList(self, head: ListNode) -> ListNode:
        new = None
        while head:
            new = ListNode(head.val, new)
            head = head.next
        return new
    
    # 3rd solution
    # O(n) time | O(1) space
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return head
        node, head.next.next, head.next = self.reverseList(head.next), head, None
        return node