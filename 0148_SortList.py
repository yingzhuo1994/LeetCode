# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 1st brute-force solution
        # O(n^2) time | O(1) space
        newHead = head
        while newHead:
            smallest = newHead
            p = newHead
            while p:
                if p.val < smallest.val:
                    smallest = p
                p = p.next
            newHead.val, smallest.val = smallest.val, newHead.val  
            newHead = newHead.next
        return head