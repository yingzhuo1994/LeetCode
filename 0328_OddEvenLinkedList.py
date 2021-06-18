# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1st solution
    # O(n) time | O(1) space
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        oddNode = head
        evenHead = head.next
        evenNode = evenHead
        while oddNode and oddNode.next and evenNode and evenNode.next:
            oddNode.next = oddNode.next.next
            evenNode.next = evenNode.next.next 
            oddNode = oddNode.next
            evenNode = evenNode.next
        oddNode.next = evenHead
        return head
        