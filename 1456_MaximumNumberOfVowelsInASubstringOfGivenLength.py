# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        ans = 0
        stack = deque([])
        for i in range(len(s)):
            if s[i] in vowels:
                stack.append(i)
            while stack and stack[0] < i - k + 1:
                stack.popleft()
            ans = max(ans, len(stack))
        return ans

