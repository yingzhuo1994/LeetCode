# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(n) space
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        p = head
        while p:
            num = num * 10 + int(p.val)
            p = p.next
        if num == 0:
            return head
        num *= 2
        prev = None
        while num > 0:
            val = num % 10
            node = ListNode(val, prev)
            prev = node
            num //= 10
        return prev