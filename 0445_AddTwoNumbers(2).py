# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(n) space
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nodeOne = self.reverse(l1)
        nodeTwo = self.reverse(l2)

        sentinel = ListNode()
        p = sentinel
        carry = 0
        while nodeOne or nodeTwo or carry:
            v1 = nodeOne.val if nodeOne else 0
            v2 = nodeTwo.val if nodeTwo else 0
            v = v1 + v2 + carry
            carry = v // 10
            r = v % 10
            node = ListNode(r)
            p.next = node
            p = p.next

            if nodeOne:
                nodeOne = nodeOne.next
            if nodeTwo:
                nodeTwo = nodeTwo.next

        return self.reverse(sentinel.next)
        
    def reverse(self, head):
        prev = None
        node = head
        while node:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
        return prev