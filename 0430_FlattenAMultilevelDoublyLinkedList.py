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