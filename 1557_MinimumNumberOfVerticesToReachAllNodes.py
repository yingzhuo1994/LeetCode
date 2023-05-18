# 1st solution
# O(E) time | O(n) space
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inCount = [0 for _ in range(n)]
        for a, b in edges:
            inCount[b] += 1
        
        return [node for node in range(n) if inCount[node] == 0]

# 2nd solution
# O(E) time | O(n) space
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(range(n)) - set(j for i, j in edges))