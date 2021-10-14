class Solution:
    # 1st hash table
    # O(n) time | O(n) space
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] not in nums[:i] and nums[i] not in nums[i+1:]:
                return nums[i]

    # 2nd solution, using set
    # O(n) time | O(n) space
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

    # 3rd solution, XOR
    # O(n) time | O(1) space
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums, 0)