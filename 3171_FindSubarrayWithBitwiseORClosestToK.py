# 1st solution
# O(n * log(U)) time | O(1) space
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf
        for i, x in enumerate(nums):
            ans = min(ans, abs(x - k))
            j = i - 1
            # 如果 x 是 nums[j] 的子集，就退出循环
            while j >= 0 and nums[j] | x != nums[j]:
                nums[j] |= x
                ans = min(ans, abs(nums[j] - k))
                j -= 1
        return ans


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf
        left = bottom = right_or = 0
        for right, x in enumerate(nums):
            right_or |= x
            while left <= right and nums[left] | right_or > k:
                ans = min(ans, (nums[left] | right_or) - k)
                if bottom <= left:
                    # 重新构建一个栈
                    # 由于 left 即将移出窗口，只需计算到 left+1
                    for i in range(right - 1, left, -1):
                        nums[i] |= nums[i + 1]
                    bottom = right
                    right_or = 0
                left += 1
            if left <= right:
                ans = min(ans, k - (nums[left] | right_or))
        return ans