# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(1) space
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        p = sentinel
        node = head
        while node:
            if node.next and node.val == node.next.val:
                value = node.val
                while node and node.val == value:
                    node = node.next
            else:
                p.next = node
                p = p.next
                nextNode = node.next
                node.next = None
                node = nextNode
        return sentinel.next
