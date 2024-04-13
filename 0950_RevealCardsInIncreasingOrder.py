# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        def reorder(array, useStart):
            n = len(array)
            if n == 1:
                return array
            mid = n // 2

            ans = [0 for _ in range(n)]
            if n & 1:
                array1 = array[:mid+1]
                array2 = reorder(array[mid + 1:], False)
            else:
                array1 = array[:mid]
                array2 = reorder(array[mid:], True)
            
            if useStart:
                for i in range(len(array1)):
                    ans[i*2] = array1[i]
                for i in range(len(array2)):
                    ans[i*2+1] = array2[i]
            else:
                if n & 1:
                    ans[0] = array1[-1]
                    for i in range(len(array1) - 1):
                        ans[1+i*2] = array[i]
                    for i in range(len(array2)):
                        ans[2+i*2] = array2[i]
                else:
                    ans[0] = array2[-1]
                    for i in range(len(array1)):
                        ans[1+i*2] = array[i]
                    for i in range(len(array2) - 1):
                        ans[2+i*2] = array2[i]

            return ans
        
        return reorder(deck, True)

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        queue = deque()
        for num in deck:
            queue.append(num)
            if len(queue) == len(deck):
                break
            queue.append(queue.popleft())
        return list(queue)[::-1]

# 3rd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        stack = deque()
        for num in deck:
            if stack:
                stack.appendleft(stack.pop())
            stack.appendleft(num)
        return list(stack)