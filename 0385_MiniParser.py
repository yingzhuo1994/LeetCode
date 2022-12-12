# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def helper(idx):
            nestedInteger = NestedInteger()
            i = idx
            stack = []
            while i < len(s):
                if s[i] == "[":
                    lst, i = helper(i + 1)
                    nestedInteger.add(lst)
                    i -= 1
                elif s[i] == "]":
                    if len(stack) > 0:
                        num = int("".join(stack))
                        stack = []
                        nestedInteger.add(NestedInteger(num))
                    return nestedInteger, i + 1
                elif s[i] == ",":
                    if len(stack) > 0:
                        num = int("".join(stack))
                        stack = []
                        nestedInteger.add(NestedInteger(num))
                else:
                    stack.append(s[i])
                i += 1
            if len(stack) > 0:
                num = int("".join(stack))
                stack = []
                nestedInteger.add(NestedInteger(num))            
            return nestedInteger
        
        if s[0] != "[":
            return NestedInteger(int(s))
        ans = helper(0)
        return ans.getList()[0]
