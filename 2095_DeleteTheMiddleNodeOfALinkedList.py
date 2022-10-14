# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        sentinel = ListNode(0, head)
        p = sentinel
        mid = length // 2
        for _ in range(mid):
            p = p.next
        p.next = p.next.next
        return sentinel.next
