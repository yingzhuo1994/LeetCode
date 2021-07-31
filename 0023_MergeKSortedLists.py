# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1st soltuion, brute force
    # O(N log(N)) time | O(N) space
    # where k is the number of linked lists and N is the total number of nodes.
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.nodes = []
        head = point = ListNode(0)
        for p in lists:
            while p:
                self.nodes.append(p.val)
                p = p.next
        
        for v in sorted(self.nodes):
            point.next = ListNode(v)
            point = point.next
        return head.next

    # 2nd soltuion, Merge lists one by one
    # O(kN) time | O(1) space
    # where k is the number of linked lists and N is the total number of nodes.
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
