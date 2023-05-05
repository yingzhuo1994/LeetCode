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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        ans = 0
        start = 0
        count = 0
        for i in range(len(s)):
            if s[i] in vowels:
                count += 1
            if start < i - k + 1:
                if s[start] in vowels:
                    count -= 1
                start += 1
            ans = max(ans, count)
        return ans