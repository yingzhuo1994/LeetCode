# 1st solution
# O(n) time | O(1) space
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def getLongestPair(start, end, t):
            ans = 0
            leftCount = 0
            rightCount = 0
            if t > 0:
                leftParen = "("
            else:
                leftParen = ")"
                
            for i in range(start, end, t):
                if s[i] == leftParen:
                    leftCount += 1
                else:
                    rightCount += 1
                if rightCount > leftCount:
                    leftCount = 0
                    rightCount = 0
                elif rightCount == leftCount:
                    ans = max(ans, leftCount * 2)
            return ans
        return max(getLongestPair(0, len(s), 1), getLongestPair(len(s) - 1, -1, -1))