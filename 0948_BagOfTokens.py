# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = 0
        ans = 0
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                ans = max(ans, score)
            elif score > 0:
                score -= 1
                power += tokens[right]
                right -= 1
                ans = max(ans, score)
            else:
                break
        return ans