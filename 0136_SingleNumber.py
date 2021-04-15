class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 1st hash table
        # O(n) time | O(n) space
        # for i in range(len(nums)):
        #     if nums[i] not in nums[:i] and nums[i] not in nums[i+1:]:
        #         return nums[i]

        # using set
        # O(n) time | O(n) space
        return 2 * sum(set(nums)) - sum(nums)
