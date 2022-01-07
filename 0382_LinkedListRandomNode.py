# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = self.getLength(head)

    def getRandom(self) -> int:
        idx = random.randint(0, self.length - 1)
        p = self.head
        while idx > 0:
            p = p.next
            idx -= 1
        return p.val
    
    def getLength(self, p):
        n = 0
        while p:
            n += 1
            p = p.next
        return n
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()