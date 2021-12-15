# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n^2) time | O(1) space
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        
        newHead = head
        count = 0
        while newHead:
            node = newHead
            newHead = newHead.next
            prev = sentinel
            curNode = sentinel.next
            count += 1
            for i in range(count - 1):
                if node.val > curNode.val:
                    prev = curNode
                    curNode = curNode.next
                else:
                    break
            prev.next = node
            node.next = curNode
        return sentinel.next