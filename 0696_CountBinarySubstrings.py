# 1st solution
# O(n) time | O(1) space
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        zero, one = 0, 0
        prev = None
        for i in range(n):
            if s[i] == "0":
                if prev != "0":
                    zero = 1
                else:
                    zero += 1
                if zero <= one:
                    ans += 1
            else:
                if prev != "1":
                    one = 1
                else:
                    one += 1
                if one <= zero:
                    ans += 1
            prev = s[i]
        
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        lst = s.replace('01', '0 1').replace('10', '1 0').split()
        array = [len(t) for t in lst]
        return sum(min(a, b) for a, b in zip(array[:-1], array[1:]))