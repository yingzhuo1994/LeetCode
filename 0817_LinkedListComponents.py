# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(n) space 
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        values = set(nums)
        ans = 0
        p = head
        first = True
        while p:
            if p.val in values:
                if first:
                    ans += 1
                    first = False
            else:
                first = True
            p = p.next
        return ans
