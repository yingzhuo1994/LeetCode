# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        lst = []
        p = head
        while p is not None:
            if p not in lst:
                lst.append(p)
                p = p.next
            else:
                return True
        return False
