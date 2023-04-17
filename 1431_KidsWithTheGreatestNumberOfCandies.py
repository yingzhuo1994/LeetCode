# 1st soluiton
# O(n) time | O(n) space
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        largest = max(candies)
        ans = [False for _ in range(len(candies))]
        for i, candy in enumerate(candies):
            if candy + extraCandies >= largest:
                ans[i] = True
        return ans