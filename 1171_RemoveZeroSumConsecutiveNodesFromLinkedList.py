# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(n) space
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        dic = {0: sentinel}
        curSum = 0
        node = head
        needExtra = False
        while node:
            curSum += node.val
            if curSum in dic:
                dic[curSum].next = node.next
                needExtra = True
            else:
                dic[curSum] = node
            node = node.next

        if needExtra:
            return self.removeZeroSumSublists(sentinel.next)

        return sentinel.next

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = collections.OrderedDict()
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next