# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(n + 1):
            num = i
            count = 0
            while num > 0:
                if num & 1:
                    count += 1
                num >>= 1
            ans[i] = count
        return ans

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ans = [0] * (n + 1)
        stack = deque([[1, 1]])
        while stack:
            num, count = stack.popleft()
            ans[num] = count
            if num << 1 <= n:
                stack.append([num << 1, count])
            if num << 1 | 1 <= n:
                stack.append([num << 1 | 1, count + 1])
        return ans