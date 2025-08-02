# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(1) space
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        p = head
        prev2 = p.val
        p = p.next
        prev1 = p.val
        p = p.next
        idx = 2
        firstIdx = lastIdx = None
        minDist = float("inf")
        while p:
            if (prev2 > prev1 and p.val > prev1) or (prev2 < prev1 and p.val < prev1):
                if lastIdx is None:
                    firstIdx = idx - 1
                else:
                    dist = idx - 1 - lastIdx
                    minDist = min(minDist, dist)
                lastIdx = idx - 1

            prev2, prev1 = prev1, p.val
            p = p.next
            idx += 1

        if lastIdx == firstIdx:
            return [-1, -1]
        
        maxDist = lastIdx - firstIdx
        return [minDist, maxDist]