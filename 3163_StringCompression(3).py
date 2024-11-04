# 1st solution
# O(n) time | O(n) space
class Solution:
    def compressedString(self, word: str) -> str:
        lst = []
        prev = word[0]
        count = 0
        for ch in word:
            if ch == prev:
                count += 1
                if count > 9:
                    lst.append(f"{9}{prev}")
                    count -= 9
            else:
                lst.append(f"{count}{prev}")
                prev = ch
                count = 1
        if count > 0:
            lst.append(f"{count}{prev}")
        return "".join(lst)