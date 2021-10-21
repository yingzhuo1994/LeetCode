class Solution:
    # 1st solution
    # O(n^2) time | O(1) space
    def longestPalindrome(self, s: str) -> str:
        def helper(s, start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return [start + 1, end - 1]

        pair = [0, 0]
        for i in range(len(s) - 1):
            pair0 = helper(s, i, i)
            pair1 = helper(s, i, i + 1)
            if pair0[1] - pair0[0] > pair[1] - pair[0]:
                pair = pair0
            if pair1[1] - pair1[0] > pair[1] - pair[0]:
                pair = pair1
        return s[pair[0]:pair[1] + 1]
