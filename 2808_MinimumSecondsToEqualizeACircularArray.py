# 1st solution
# O(n) time | O(n) space
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = n = len(nums)
        for lst in pos.values():
            lst.append(lst[0] + n)
            mx = max(j - i for i, j in pairwise(lst)) // 2
            ans = min(ans, mx)
        return ans