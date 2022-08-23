# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1st solution
# O(n) time | O(n) space
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        start = 0
        end = len(lst) - 1
        while start <= end:
            if lst[start] != lst[end]:
                return False
            start += 1
            end -= 1
        return True

# 2nd Solution
# O(n) time | O(1) space
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        secondHalf = self.reverseLinkedList(slow.next)
        firstHalf = head
        while firstHalf and secondHalf:
            if firstHalf.val != secondHalf.val:
                return False
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        return True
    
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            p = head
            head = head.next
            p.next = prev
            prev = p
        return prev

#3rd solution
# O(n) time | O(1) space
class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
