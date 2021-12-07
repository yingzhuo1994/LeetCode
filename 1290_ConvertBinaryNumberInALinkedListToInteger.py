# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution, binary representation
# O(n) time | O(1) space
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        p = head
        while p:
            res = res * 2 + p.val
            p = p.next
        return res

# 2nd solution, bit manipulation
# O(n) time | O(1) space
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = (num << 1) | head.next.val
            head = head.next
        return num