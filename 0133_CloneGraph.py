"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# 1st solution
# O(n) time | O(n) space
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node
        createdList = {}
        headValue = node.val
        stack = [node]
        while stack:
            curNode = stack.pop()
            value = curNode.val
            if value in createdList:
                continue
            newNode = Node(value)
            createdList[value] = newNode
            for neighbor in curNode.neighbors:
                stack.append(neighbor)
        stack = [node]
        visited = set()
        while stack:
            curNode = stack.pop()
            value = curNode.val
            if value in visited:
                continue
            visited.add(value)
            for neighbor in curNode.neighbors:
                createdList[value].neighbors.append(createdList[neighbor.val])
                stack.append(neighbor)
        return createdList[headValue]