# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(n) space
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        start, end = 0, len(lst) - 1
        ans = 0
        while start < end:
            ans = max(ans, lst[start] + lst[end])
            start += 1
            end -= 1
        
        return ans