# 1st solution
# O(n) time | O(n) space
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        inCount = [0 for _ in range(n)]
        for i in range(n):
            if leftChild[i] != -1:
                inCount[leftChild[i]] += 1
            if rightChild[i] != -1:
                inCount[rightChild[i]] += 1
        
        roots = [node for node in range(n) if inCount[node] == 0]
        if len(roots) != 1:
            return False
        
        if any(inCount[node] > 1 for node in range(n)):
            return False
        # print(roots)
        visited = [False for _ in range(n)]
        def dfs(node):
            if node == -1:
                return True
            # print(node)
            if visited[node]:
                return False
            visited[node] = True
            if not dfs(leftChild[node]):
                return False
            if not dfs(rightChild[node]):
                return False
            return True

        if not dfs(roots[0]):
            return False
        
        return all(visited)

