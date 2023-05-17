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

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        fastNode = head
        prev = None
        while fastNode and fastNode.next:
            fastNode = fastNode.next.next
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode

        ans = 0
        while node:
            ans = max(ans, prev.val + node.val)
            node = node.next
            prev = prev.next

        return ans