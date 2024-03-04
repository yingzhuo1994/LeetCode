# 1st solution
# O(k^n) time | O(k^n) space
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        ans = list()
        nodeNum = k**(n-1)
        edges = [k-1]*nodeNum

        node = 0
        while edges[node] >= 0:
            edge = edges[node]
            edges[node] -= 1
            node = (node * k + edge) % nodeNum
            ans.append(str(edge))
    
        return  "0"*(n-1)  + "".join(ans)