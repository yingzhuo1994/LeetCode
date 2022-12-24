# 1st solution
# O(n) time | O(1) space
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        curSum = 0
        ans = 0
        if n + 1 > nums[-1]:
            nums.append(n + 1)
        for num in nums:
            if curSum >= n:
                break
            while curSum < num - 1:
                curSum += curSum + 1
                ans += 1
                if curSum >= n:
                    return ans
            curSum += num
        return ans