# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        dic = {num: 1 for num in nums}
        for num in nums:
            sq = num * num
            if sq in dic:
                dic[sq] = max(dic[sq], dic[num] + 1)
        ans = max(dic.values())
        if ans == 1:
            return -1
        return ans


# 2nd solution
# O(n) time | O(n) space
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s = set(nums)
        @cache
        def dfs(x: int) -> int:
            if x not in s: 
                return 0
            return 1 + dfs(x * x)
        ans = max(map(dfs, s))
        return ans if ans > 1 else -1