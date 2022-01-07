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
        
# 2nd solution
class Solution:
    # O(n) time | O(n) space
    def __init__(self, head: Optional[ListNode]):
        self.stack = []
        while head:
            self.stack.append(head.val)
            head = head.next

    # O(1) time | O(1) space
    def getRandom(self) -> int:
        idx = random.randint(0, len(self.stack) - 1)
        return self.stack[idx]

# 3rd solution, Reservoir Sampling
class Solution:
    # O(1) time | O(1) space
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    # O(n) time | O(1) space
    def getRandom(self) -> int:
        scope = 1
        chosen_value = 0
        curr = self.head

        while curr:
            # decide whether to include the element in reservoir
            if random.random() < 1 / scope:
                chosen_value = curr.val
            # move on to the next node
            curr = curr.next
            scope += 1
        return chosen_value

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()