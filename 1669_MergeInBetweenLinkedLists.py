# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(1) space
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        sentinel = ListNode(next=list1)
        p = sentinel
        prevNodeA = None
        nodeB = None
        for i in range(b + 1):
            if i == a:
                prevNodeA = p
            if i == b:
                nodeB = p.next
            p = p.next
        prevNodeA.next = list2
        q = list2
        while q.next:
            q = q.next
        q.next = nodeB.next
        nodeB.next = None
        return sentinel.next