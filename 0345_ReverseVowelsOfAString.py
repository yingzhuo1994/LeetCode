class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        stack = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if stack[left].lower() not in vowels:
                left += 1
                continue
            if stack[right].lower() not in vowels:
                right -= 1
                continue
            stack[left], stack[right] = stack[right], stack[left]
            left += 1
            right -= 1
        return "".join(stack)
