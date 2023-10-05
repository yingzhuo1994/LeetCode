# 1st solution
# O(mn) time | O(max(m, n)) space
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        aCount = Counter(a)
        bCount = Counter(b)
        for ch in bCount:
            if ch not in aCount:
                return -1
        
        for i in range(len(a)):
            left = len(a) - i
            if left < len(b):
                repeat, r = divmod(len(b) - left, len(a))
                repeat += 1
                if r > 0:
                    repeat += 1
            else:
                repeat = 1
            s = a * repeat

            if b == s[i:i+len(b)]:
                return repeat

        return -1