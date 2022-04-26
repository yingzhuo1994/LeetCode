# 1st solution
# O(n) time | O(1) space
class Solution:
    def secondHighest(self, s: str) -> int:
        first = float("-inf")
        second = first
        for ch in s:
            if ch.isdigit():
                if int(ch) > first:
                    first, second = int(ch), first
                elif int(ch) > second and int(ch) != first:
                    second = int(ch)
        return second if second != float("-inf") else -1