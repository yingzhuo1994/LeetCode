# 1st solution
# O(n) time | O(n) space
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        stack = [1]
        while len(stack) < n:
            num = stack[-1]
            if num * 10 <= n:
                num *= 10
            else:
                if num + 1 <= n:
                    num += 1
                else:
                    num //= 10
                    num += 1
                while num % 10 == 0:
                    num //= 10
            stack.append(num)         
        return stack

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = [1]
        while len(ans) < n:
            new = ans[-1] * 10
            while new > n:
                new //= 10
                new += 1
                while new % 10 == 0:    # deal with case like 199+1=200 when we need to restart from 2.
                    new //= 10
            ans.append(new)    
        return ans