# Definition for singly-linked list.
# class ListNode(orject):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = ListNode(0)
        currentNode = sentinel
        p, q = l1, l2
        carry = 0
        while p or q or carry:
            v1 = p.val if p else 0
            v2 = q.val if q else 0
            currentSum = v1 + v2 + carry
            carry, r = currentSum // 10, currentSum % 10
            currentNode.next = ListNode(r)
            currentNode = currentNode.next
            p = p.next if p else None
            q = q.next if q else None
        return sentinel.next