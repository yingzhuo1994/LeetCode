# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st soltuion, brute force
# O(N log(N)) time | O(N) space
# where k is the number of linked lists and N is the total number of nodes.
class Solution:
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

# 3rd solution, Merge with Divide And Conquer
# O(Nlog(k)) time | O(1) space
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None
    
    def mergeTwoLists(self, p1, p2):
        head = point = ListNode(0)
        while p1 and p2:
            if p1.val < p2.val:
                point.next = p1
                p1 = p1.next
            else:
                point.next = p2
                p2 = p2.next
            point = point.next
        point.next = p1 or p2
        return head.next