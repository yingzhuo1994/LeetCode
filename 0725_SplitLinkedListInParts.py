# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        p = head
        while p is not None:
            n += 1
            p = p.next
        partLength = n // k
        remainder = n % k
        result = []
        p = head
        extra = 1
        for i in range(k):
            sentinel = ListNode(0)
            curNode = sentinel
            if remainder <= 0:
                extra = 0
            for j in range(partLength + extra):
                curNode.next = p
                p = p.next
                curNode = curNode.next
            remainder -= 1
            curNode.next = None
            result.append(sentinel.next)
        return result