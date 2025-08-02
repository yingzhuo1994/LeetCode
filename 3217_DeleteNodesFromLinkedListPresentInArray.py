# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n + k) time | O(k) space
# where k = len(nums), n is length of the Linked List
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        sentinel = ListNode()
        p = sentinel
        node = head
        while node:
            nextNode = node.next
            if node.val not in nums:
                p.next = node
                p = p.next
            node.next = None
            node = nextNode
        return sentinel.next
            