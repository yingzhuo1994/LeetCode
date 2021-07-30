# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = lists[0]
        for i in range(1, len(lists)):
            p = sentinel
            q = lists[i]
            while p.next and q:
                if p.next.val > q.val:
                    temp = q
                    q = q.next
                    temp.next = p.next
                    p.next = temp
                p = p.next
            if q:
                p.next = q
        return sentinel.next
