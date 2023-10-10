# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        robots = [[loc, dirc] for loc, dirc in zip(nums, s)]

        new = [0 for _ in range(n)]

        for i in range(n):
            loc, dirc = robots[i]
            if dirc == "L":
                new[i] = loc - d
            else:
                new[i] = loc + d
        
        new.sort()
        
        MOD = 10**9 + 7
        ans = 0
        dist = 0

        for i in range(1, n):
            last = new[i] - new[i - 1]
            dist += i* last
            ans += dist
            ans %= MOD

        return ans 