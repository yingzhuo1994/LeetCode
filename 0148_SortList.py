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

        # 2nd merge sort solution
        # O(nlogn) time | O(1) space
                if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

        def merge(self, list1, list2):
            dummyHead = ListNode(0)
            tail = dummyHead
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                    tail = tail.next
                else:
                    tail.next = list2
                    list2 = list2.next
                    tail = tail.next

            tail.next = list1 if list1 != None else list2
            return dummyHead.next

        def getMid(self, head):
            midPrev = None
            while head != None and head.next != None:
                midPrev = head if midPrev == None else midPrev.next
                head = head.next.next
            mid = midPrev.next
            midPrev.next = None
            return mid

