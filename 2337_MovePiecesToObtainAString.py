# 1st solution
# O(m + n) time | O(1) space
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i, j = 0, 0
        while i < len(start) and j < len(target):
            if start[i] == "_":
                i += 1
            elif target[j] == "_":
                j += 1
            else:
                if start[i] != target[j]:
                    return False
                if start[i] == "L" and j <= i:
                    i += 1
                    j += 1
                elif start[i] == "R" and j >= i:
                    i += 1
                    j += 1
                else:
                    return False
        while i < len(start) and start[i] == "_":
            i += 1
        while j < len(target) and target[j] == "_":
            j += 1
        return i == len(start) and j == len(target)