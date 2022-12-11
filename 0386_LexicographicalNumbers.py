# 1st solution
# O(n) time | O(n) space
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        num = 1
        stack = []
        while len(stack) < n:
            stack.append(num)
            if num * 10 <= n:
                num *= 10
            elif num + 1 <= n:
                num += 1
                while num % 10 == 0:
                    num //= 10
            else:
                num //= 10
                if num == 0 or num == 9:
                    break
                num += 1
                while num % 10 == 0:
                    num //= 10                
        return stack