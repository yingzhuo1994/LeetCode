"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # 1st solution
    # O(n) time | O(n) space
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
    
    # 2nd solution
    # O(n) time | O(1) space
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        
        # First round: make copy of each node, and link them together side-by-side in a single list
        cur = head
        while cur:
            nextNode = cur.next
            cur.next = Node(cur.val, nextNode, None)
            cur = nextNode
        
        # Second round: assign random pointers for the copy nodes
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        # Third round: restore the original list, and extract the copy list
        cur = head
        newHead = head.next
        while cur:
            nextNode = cur.next.next
            
            copy = cur.next
            cur.next = nextNode
            
            if nextNode:
                copy.next = nextNode.next
            cur = nextNode
        
        return newHead
        