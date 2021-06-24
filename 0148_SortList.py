# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1st brute-force solution
    # O(n^2) time | O(1) space
    def sortList(self, head: ListNode) -> ListNode:
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
    # O(nlogn) time | O(n) space
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, list1, list2):
        sentinel = ListNode(0)
        tail = sentinel
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return sentinel.next

    def getMid(self, head):
        midPrev = None
        while head and head.next:
            midPrev = head if midPrev == None else midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid
        
    # 3rd solution
    # O(nlogn) time | O(n) space
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        temp = head
        data = []
        while temp is not None:
            data.append(temp.val)
            temp = temp.next
        temp = head
        data = sorted(data)
        for num in data:
            temp.val = num
            temp = temp.next
        return head        

    # 4th solution
    # O(nlogn) time | O(1) space
    tail = ListNode()
    nextSublist = ListNode()
    
    def sortList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head
        n = self.getCount(head)
        start = head
        dummyHead = ListNode()
        size = 1
        while size < n:
            Solution.tail = dummyHead
            while start != None:
                if not start.next:
                    Solution.tail.next = start
                    break
                mid = self.split(start, size)
                self.merge(start, mid)
                start = Solution.nextSubList
            start = dummyHead.next
            size = size * 2
        return dummyHead.next

    def split(self, start, size):

        midPrev = start
        end = start.next
        # use fast and slow approach to find middle and end of second linked list
        index = 1
        while index < size and (midPrev.next or end.next):
            if end.next:
                end = end.next.next if end.next.next else end.next
            if midPrev.next:
                midPrev = midPrev.next
            index += 1

        mid = midPrev.next
        midPrev.next = None
        Solution.nextSubList = end.next
        end.next = None
        # return the start of second linked list
        return mid

    def merge(self, list1, list2):
        dummyHead = ListNode()
        newTail = dummyHead
        while list1 and list2:
            if list1.val < list2.val:
                newTail.next = list1
                list1 = list1.next
            else:
                newTail.next = list2
                list2 = list2.next

            newTail = newTail.next

        newTail.next = list1 or list2
        # traverse till the end of merged list to get the newTail
        while newTail.next:
            newTail = newTail.next
    
        # link the old tail with the head of merged list
        Solution.tail.next = dummyHead.next
        # update the old tail to the new tail of merged list
        Solution.tail = newTail

    def getCount(self, head):
        cnt = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            cnt += 1
        return cnt

