"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        sentinel = Node(0)
        newHead = sentinel
        p = head
        originalNodeLst = []
        newNodeLst = []
        while p:
            newHead.next = Node(p.val)
            newHead = newHead.next
            newNodeLst.append(newHead)
            originalNodeLst.append(p)
            p = p.next
        for i, node in enumerate(originalNodeLst):
            if node.random:
                index = originalNodeLst.index(node.random)
                newNodeLst[i].random = newNodeLst[index]
        return sentinel.next
        