# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        
        node = head
        while node.next:
            g = gcd(node.val, node.next.val)
            nextNode = node.next
            node.next = ListNode(g, nextNode)
            node = nextNode
        
        return head