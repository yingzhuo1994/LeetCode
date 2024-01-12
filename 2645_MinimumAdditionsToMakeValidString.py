# 1st solution
# O(n) time | O(1) space
class Solution:
    def addMinimum(self, word: str) -> int:
        ans = 0
        prev = "c"
        for i, ch in enumerate(word + "a"):
            if ch == "c":
                if prev == "b":
                    pass
                elif prev == "a":
                    ans += 1
                else:
                    ans += 2
            elif ch == "b":
                if prev == "a":
                    pass
                elif prev == "b":
                    ans += 2
                else:
                    ans += 1
            elif ch == "a":
                if prev == "c":
                    pass
                elif prev == "a":
                    ans += 2
                else:
                    ans += 1
            prev = ch
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def addMinimum(self, word: str) -> int:
        k, prev = 0, 'z'
        for c in word:
            k += c <= prev
            prev = c
        return k * 3 - len(word)