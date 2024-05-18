# 1st solution
# O(n^2) time | O(1) space
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans = divisors[0]
        count = 0
        for divisor in divisors:
            score = 0
            for num in nums:
                if num % divisor == 0:
                    score += 1
            if score > count:
                count = score
                ans = divisor
            elif score == count:
                ans = min(ans, divisor)
        return ans
