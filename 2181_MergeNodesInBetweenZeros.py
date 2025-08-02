# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        p = sentinel
        val = 0
        node = head.next
        while node:
            if node.val == 0:
                p.next = ListNode(val)
                p = p.next
                val = 0
            else:
                val += node.val
            node = node.next
        return sentinel.next