# 1st solution
# O(n) time | O(n) space
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        array = []
        for ch in s:
            if ch != "-":
                array.append(ch.upper())
        ans = []
        n = len(array)
        start = n % k
        if start != 0:
            ans.append("".join(array[:start]))
        for i in range(start, n, k):
            ans.append("".join(array[i:i+k]))
        return "-".join(ans)

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        keys = s.upper().replace('-','')
        n = len(keys)
        start = n % k
        ans = []
        if start != 0:
            ans.append(keys[:start])
        for i in range(start, n, k):
            ans.append("".join(keys[i:i+k]))
        return "-".join(ans)