# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1st solution
# O(n) time | O(n) space
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        lst = set()
        p = head
        while p is not None:
            if p not in lst:
                lst.add(p)
                p = p.next
            else:
                return True
        return False

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Faster solution
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
