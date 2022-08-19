# 1st solution
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        minStack = deque()
        for num in nums:
            newStack = deque()
            while minStack and num == minStack[0][0]:
                stack = minStack.popleft()
                newStack.append(stack)
            
            while minStack and num - 1 != minStack[0][0]:
                stack = minStack.popleft()
                if stack[1] < 3:
                    return False
            
            if not minStack:
                minStack.append([num, 1])
            elif num - 1 == minStack[0][0]:
                stack = minStack.popleft()
                stack[0] += 1
                stack[1] += 1
                newStack.append(stack)
            minStack.extend(newStack)
            # print(num, minStack)
                
        for _, length in minStack:
            if length < 3:
                return False
        return True

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = collections.Counter(nums)
        end = collections.Counter()
        for num in nums:
            if not left[num]: continue
            left[num] -= 1
            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
            elif left[num + 1] and left[num + 2]:
                left[num + 1] -= 1
                left[num + 2] -= 1
                end[num + 2] += 1
            else:
                return False
        return True