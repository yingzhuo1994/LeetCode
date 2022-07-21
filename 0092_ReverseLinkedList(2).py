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
        idx = 0
        while idx + 1 < left:
            p = p.next
            idx += 1
        
        newHead = p
        startNode = p.next
        p = p.next
        idx += 1
        
        prev = None
        while idx <= right:
            nextNode = p.next
            p.next = prev
            prev = p
            p = nextNode
            idx += 1
        newHead.next = prev
        startNode.next = p
        
        return sentinel.next