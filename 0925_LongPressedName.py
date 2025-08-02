# 1st solution
# O(max(m, n)) time | O(1) space
# where m = len(name) and n = len(typed)
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        if i != len(name):
            return False
        while j < len(typed) and typed[j] == name[-1]:
            j += 1
        return j == len(typed)

# 2nd solution
# O(max(m, n)) time | O(1) space
# where m = len(name) and n = len(typed)
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        return i == len(name)