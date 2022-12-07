# 1st solution
# O(log(n)) time | O(log(n)) space
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        visited = set([n])
        stack = deque([[n, 1]])
        while stack:
            num, step = stack.popleft()
            if num & 1:
                if num - 1 == 1 or num + 1 == 1:
                    return step
                if num - 1 not in visited:
                    stack.append([num - 1, step + 1])
                    visited.add(num - 1)
                if num + 1 not in visited:
                    stack.append([num + 1, step + 1])
                    visited.add(num + 1)
            else:
                if num // 2 == 1:
                    return step
                if num // 2 not in visited:
                    stack.append([num // 2, step + 1])
                    visited.add(num // 2)
                
# 2nd solution
# O(log(n)) time | O(log(1)) space
class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n > 1:
            count += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return count