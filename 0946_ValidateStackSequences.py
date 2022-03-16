# 1st solution
# O(n) time | O(n) space
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popIdx = 0
        for num in pushed:
            stack.append(num)
            while len(stack) > 0 and stack[-1] == popped[popIdx]:
                stack.pop()
                popIdx += 1
        return len(stack) == 0 and popIdx == len(popped)

