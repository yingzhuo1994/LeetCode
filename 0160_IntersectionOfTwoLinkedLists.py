# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # lstA = []
        # lstB = []
        # while headA is not None:
        #     lstA.append(headA)
        #     headA = headA.next
        # while headB is not None:
        #     lstB.append(headB)
        #     headB = headB.next
        # intersection = None
        # for i in range(1, min(len(lstA), len(lstB)) + 1):
        #     if lstA[-i] == lstB[-i]:
        #         intersection = lstA[-i]
        #     else:
        #         break
        # return intersection

        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None
