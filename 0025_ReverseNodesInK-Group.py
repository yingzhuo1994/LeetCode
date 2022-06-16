# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(1) space
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head:
            return head
        length = self.getLength(head)
        sentinel = ListNode(0)
        p = sentinel
        curNode = head
        idx = 0
        while idx + k <= length:
            lastHead, lastTail = self.reverse(curNode, k)
            p.next = lastHead
            p = lastTail
            curNode = lastTail.next
            idx += k
        return sentinel.next
        
    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
    
    def reverse(self, curNode, k):
        prev = None
        tailNode = curNode
        for i in range(k):
            nextNode = curNode.next
            curNode.next = prev
            prev = curNode
            curNode = nextNode
        headNode = prev
        tailNode.next = curNode
        return headNode, tailNode