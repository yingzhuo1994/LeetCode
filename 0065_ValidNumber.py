# O(n) time | O(1) space
class Solution:
    def isNumber(self, s: str) -> bool:
        i = 0
        if s[i] in "+-":
            i += 1
        
        intLength = 0
        while i < len(s) and s[i].isdigit():
            intLength += 1
            i += 1
        
        decimalLength = 0
        containDecimal = False
        if i < len(s) and s[i] == ".":
            i += 1
            containDecimal = True
            while i < len(s) and s[i].isdigit():
                decimalLength += 1
                i += 1
        expLength = 0
        containExp = False
        if i < len(s) and s[i] in "Ee":
            i += 1
            containExp = True
            if i < len(s) and s[i] in "+-":
                i += 1
            while i < len(s) and s[i].isdigit():
                expLength += 1
                i += 1
        if i != len(s):
            return False
        if containDecimal:
            if intLength == 0 and decimalLength == 0:
                return False
        else:
            if intLength == 0:
                return False
        if containExp:
            if expLength == 0:
                return False
        return True
