# 1st solution
# O(kn) time | O(n) space
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        dic = {i: Node(i) for i in range(1, n + 1)}
        for i in range(1, n):
            dic[i].next = dic[i+1]
            dic[i+1].prev = dic[i]
        dic[n].next = dic[1]
        dic[1].prev = dic[n]
        count = n
        node = dic[1]
        while count > 1:
            for _ in range(k - 1):
                node = node.next
            nextNode = node.next
            node.prev.next = node.next
            node.next.prev = node.prev
            node = nextNode
            count -= 1
        return node.val

class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


# 2nd solution
# O(kn) time | O(n) space
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque([i for i in range(1, n + 1)])
        while len(queue) > 1:
            for _ in range(k - 1):
                node = queue.popleft()
                queue.append(node)
            queue.popleft()
        return queue[0]


# 3rd solution
# O(n) time | O(n) space
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return 1 if n == 1 else (k + self.findTheWinner(n - 1, k) - 1) % n + 1
    

# 4th solution
# O(n) time | O(1) space
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 1
        for i in range(2, n + 1):
            winner = (k + winner - 1) % i + 1
        return winner