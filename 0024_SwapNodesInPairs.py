# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution, recursion
# O(n) time | O(n) space
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nextNode = head.next.next
        first = head
        second = head.next
        second.next = first
        first.next = self.swapPairs(nextNode)
        head = second
        return head

# 2st solution, iteration
# O(n) time | O(1) space
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        sentinel = ListNode(0)
        lastNode = sentinel
        first = head
        second = head.next
        while first and second:
            nextNode = second.next
            lastNode.next = second
            second.next = first
            lastNode = first
            first = nextNode
            second = nextNode.next if nextNode else None
        lastNode.next = first or second
        return sentinel.next