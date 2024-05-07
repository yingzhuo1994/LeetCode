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


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)
        node = head
        while node:
            node.val = (node.val * 2) % 10
            if node.next and node.next.val > 4:
                node.val += 1
            node = node.next
        return head