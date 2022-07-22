# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time | O(1) space
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        
        firstHead = ListNode(0)
        secondHead = ListNode(0)

        curNode = head
        p1 = firstHead
        p2 = secondHead
        while curNode:
            if curNode.val < x:
                p1.next = curNode
                p1 = p1.next
            else:
                p2.next = curNode
                p2 = p2.next
            curNode = curNode.next
        
        p1.next = secondHead.next
        p2.next = None
        return firstHead.next