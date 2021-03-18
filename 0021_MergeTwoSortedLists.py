# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 1st solution
        # result = ListNode(0)
        # result_tail = result
        # p, q = l1, l2
        # while p or q:
        #     x = p.val if p else None
        #     y = q.val if q else None
        #     if p and q:
        #         if x < y:
        #             result_tail.next = ListNode(x)
        #             p = p.next
        #         else:
        #             result_tail.next = ListNode(y)
        #             q = q.next
        #     elif p and not q:
        #         result_tail.next = ListNode(x)
        #         p = p.next
        #     elif not p and q:
        #         result_tail.next = ListNode(y)
        #         q = q.next
        #     result_tail = result_tail.next
        # return result.next

        # 2nd solution iteratively
        if None in (l1, l2):
            return l1 or l2
        result = ListNode(0)
        p = result
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 or l2
        return result.next
