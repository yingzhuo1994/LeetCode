# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(1) space
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        sentinel = ListNode(0)
        sentinel.next = head
        p = sentinel
        idx = 1
        while idx < left:
            p = p.next
            idx += 1
        
        newHead = p
        leftNode = p.next
        p = p.next
        idx += 1
        
        while idx <= right:
            p = p.next
            idx += 1
        newTail = p.next

        curNode = leftNode
        prev = newTail
        while curNode != newTail:
            nextNode = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = nextNode
        newHead.next = prev
        
        return sentinel.next