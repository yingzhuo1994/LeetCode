# 1st solution
# O(n + q) time | O(n) space
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        nodes = {i: Node(i) for i in range(n)}
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
            nodes[i + 1].prev = nodes[i]

        ans = []
        shortest = n -1
        for u, v in queries:
            if u != 0 and nodes[u].prev is None:
                ans.append(shortest)
            elif v != n - 1 and nodes[v].next is None:
                ans.append(shortest)
            else:
                startNode = nodes[u]
                count = 0
                node = nodes[u].next
                while node.val < v:
                    startNode.next = node.next
                    node.next.prev = startNode
                    node.prev = None
                    node.next = None
                    node = startNode.next
                    count += 1
                shortest -= count
                ans.append(shortest)
        return ans

class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


# 2nd solution
# O(n + k) time | O(n) space
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        nxt = list(range(1, n))
        cnt = n - 1
        for i, r in queries:
            while nxt[i] < r:
                cnt -= 1
                nxt[i], i = r, nxt[i]
            ans.append(cnt)
        return ans