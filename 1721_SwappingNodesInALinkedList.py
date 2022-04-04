# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(1) space
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode(0)
        sentinel.next = head
        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        
        moveFrontSetps = min(k, length + 1 - k)
        moveBackSteps = max(k, length + 1 - k)

        if moveFrontSetps != moveBackSteps:
            frontNode = self.removeNode(sentinel, moveFrontSetps)
            backNode = self.removeNode(sentinel, moveBackSteps - 1)

            self.insertAt(sentinel, moveFrontSetps, backNode)
            self.insertAt(sentinel, moveBackSteps, frontNode)

        return sentinel.next

    def removeNode(self, sentinel, steps):
        p = sentinel
        while steps > 1:
            p = p.next
            steps -= 1
        node = p.next
        p.next = node.next
        node.next = None
        return node
    
    def insertAt(self, sentinel, steps, node):
        p = sentinel
        while steps > 1:
            p = p.next
            steps -= 1
        nextNode = p.next
        p.next = node
        node.next = nextNode
