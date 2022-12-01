class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        isOdd = False
        ans = 0
        for v in count.values():
            if v & 1:
                if isOdd:
                    ans += v - 1
                else:
                    ans += v
                    isOdd = True
            else:
                ans += v
        return ans