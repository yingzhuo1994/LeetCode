# 1st solution
# O(mn) time | O(1) space
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


# 2st solution
# O(mn + m * log(m) + n * log(n)) time | O(1) space
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        nums.sort(reverse=True)
        dup = sum(1 for x, y in pairwise(nums) if x == y)
        divisors.sort()
        max_cnt, ans = -1, 0
        for d in divisors:
            if (max_cnt - dup + 1) * d > nums[0]:
                break
            cnt = 0
            for x in nums:
                if x < d:
                    break
                if x % d == 0:
                    cnt += 1
            if cnt > max_cnt:
                max_cnt, ans = cnt, d
        return ans