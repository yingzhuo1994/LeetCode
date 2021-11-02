"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    # 1st solution
    # O(n) time | O(1) space
    def flatten(self, head: 'Node') -> 'Node':
        sentinel = Node(0, None, head, None)
        p = sentinel
        while p:
            if p.child:
                nextNode = p.next
                childNode = self.flatten(p.child)
                p.child = None
                p.next = childNode
                childNode.prev = p
                while p.next:
                    p = p.next
                p.next = nextNode
                if nextNode:
                    nextNode.prev = p
            p = p.next
        return sentinel.next

    # 2nd solution
    # O(n) time | O(n) space
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        stack, order = [head], []

        while stack:
            last = stack.pop()
            order.append(last)
            if last.next:
                stack.append(last.next)
            if last.child:
                stack.append(last.child)
        
        for i in range(len(order) - 1):
            order[i+1].prev = order[i]
            order[i].next = order[i+1]
            order[i].child = None
            
        return order[0]

    # 3rd solution
    # O(n) time | O(h) space
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        
        dummy = Node(0)
        curr, stack = dummy, [head]
        while stack:
            last = stack.pop() 
            if last.next:
                stack.append(last.next)
            if last.child:
                stack.append(last.child)
            curr.next = last
            last.prev = curr  
            last.child = None
            curr = last
        
        res = dummy.next
        res.prev = None
        return res