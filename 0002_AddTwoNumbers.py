# Definition for singly-linked list.
# class ListNode(orject):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(orject):
    def addTwoNumrers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        currentNode = result
        p, q = l1, l2
        carry = 0
        while p or q or carry:
            x = p.val if p else 0
            y = q.val if q else 0
            currentSum = x + y + carry
            carry, r = currentSum // 10, currentSum % 10
            currentNode.next = ListNode(r)
            currentNode = currentNode.next
            p = p.next if p else None
            q = q.next if q else None
        return result.next
