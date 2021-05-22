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
        start = sentinel
        p = head
        lst = []
        while p:
            start.next = Node(p.val)
            lst.append(start.next)
            p = p.next
            start = start.next
        p = head
        start = sentinel.next
        while p:
            if p.random is None:
                p = p.next
                start = start.next
                continue
            index = 0
            searchNode = head
            while searchNode != p.random:
                searchNode = searchNode.next
                index += 1
            start.random = lst[index]
            start = start.next
            p = p.next
        return sentinel.next
        