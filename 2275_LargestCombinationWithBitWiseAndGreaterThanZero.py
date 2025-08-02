# 1st solution
# O(n * k) time | O(1) space
# where n = len(candidates) and k is the length of the largest num
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 1
        d = 24
        while d >= 0:
            count = 0
            for num in candidates:
                if (num >> d) & 1:
                    count += 1
            if count > 0:
                ans = max(ans, count)
            d -= 1
        return ans
