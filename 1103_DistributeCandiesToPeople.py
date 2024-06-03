# 1st solution
# O(sqrt(m)) time | O(n) space
# where m = candies, n = num_people
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        ans = [0] * n
        val = 1
        while candies > 0:
            idx = (val - 1) % n
            ans[idx] += min(val, candies)
            candies -= val
            val += 1
        return ans