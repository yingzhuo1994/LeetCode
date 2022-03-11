# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(1) space
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        listLength = 0
        node = head
        tail = head
        while node is not None:
            listLength += 1
            tail = node
            node = node.next
        if listLength <= 1:
            return head
        k = k % listLength
        if k == 0:
            return head
        moveStep = listLength - k
        node = head
        prevNode = None
        while moveStep > 0:
            prevNode = node
            node = node.next
            moveStep -= 1
        newHead = node
        if prevNode:
            prevNode.next = None
        tail.next = head
        return newHead
        
        