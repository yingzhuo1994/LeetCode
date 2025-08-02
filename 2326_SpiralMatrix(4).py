# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        i, j = 0, 0
        dx, dy = 0, 1
        node = head
        rowStart, rowEnd = 0, m - 1
        colStart, colEnd = 0, n - 1
        while node:
            matrix[i][j] = node.val
            node = node.next
            if j + dy > colEnd:
                dy = 0
                dx = 1
                rowStart += 1
            elif j + dy < colStart:
                dy = 0
                dx = -1
                rowEnd -= 1
            elif i + dx > rowEnd:
                dx = 0
                dy = -1
                colEnd -= 1
            elif i + dx < rowStart:
                dx = 0
                dy = 1
                colStart += 1 
            i += dx
            j += dy
        # for row in matrix:
        #     print(row)
        return matrix