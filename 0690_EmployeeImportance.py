"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# 1st solution
# O(n) time | O(n) space
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(node):
            cur = node.importance
            for subordinate in node.subordinates:
                cur += dfs(dic[subordinate])
            return cur
        dic = {node.id: node for node in employees}
        return dfs(dic[id])