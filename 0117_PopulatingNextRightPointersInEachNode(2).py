"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 1st solution
# O(n) time | O(n) space
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        level = [root]
        while level:
            nextLevel = []
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]
            for node in level:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            level = nextLevel
        return root

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curLevelNode = root
        while curLevelNode:
            nextLevelNode = sentinel = Node(0)
            while curLevelNode:
                if curLevelNode.left:
                    nextLevelNode.next = curLevelNode.left
                    nextLevelNode = nextLevelNode.next
                if curLevelNode.right:
                    nextLevelNode.next = curLevelNode.right
                    nextLevelNode = nextLevelNode.next
                curLevelNode = curLevelNode.next
            curLevelNode = sentinel.next
               
        return root