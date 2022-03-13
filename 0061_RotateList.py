# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(1) space
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        listLength = 1
        tail = head
        while tail.next:
            listLength += 1
            tail = tail.next

        k = k % listLength
        if k == 0:
            return head
        moveStep = listLength - k

        node = head
        while moveStep > 1:
            node = node.next
            moveStep -= 1
        
        newHead = node.next
        node.next = None
        tail.next = head

        return newHead
        
        