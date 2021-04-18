class MinStack:

    # 1st solution
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stack = []
    #     self.min_stack = []
    #
    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if not self.min_stack or val > self.min_stack[-1]:
    #         self.min_stack.append(val)
    #     else:
    #         start = 0
    #         end = len(self.min_stack) - 1
    #         while start < end:
    #             mid = (start + end) // 2
    #             midVal = self.min_stack[mid]
    #             if val <= midVal:
    #                 end = mid
    #             else:
    #                 start = mid + 1
    #         self.min_stack.insert(end, val)
    #
    # def pop(self) -> None:
    #     val = self.stack.pop()
    #     self.min_stack.remove(val)
    #
    # def top(self) -> int:
    #     return self.stack[-1]
    #
    # def getMin(self) -> int:
    #     return self.min_stack[0]

    # 2nd solution
    # class Node:
    #     def __init__(self, val, minVal, next = None):
    #         self.val = val
    #         self.min = minVal
    #         self.next = next
    #
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.head = None
    #
    # def push(self, val: int) -> None:
    #     if not self.head:
    #         self.head = Node(val, val)
    #     else:
    #         self.head = Node(val, min(val, self.head.min), self.head)
    #
    # def pop(self) -> None:
    #     if self.head:
    #         self.head = self.head.next
    #
    # def top(self) -> int:
    #     return self.head.val
    #
    # def getMin(self) -> int:
    #     return self.head.min

    # 3rd solution
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack= []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
