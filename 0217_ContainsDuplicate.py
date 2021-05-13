class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1st solution
        # O(n) time | O(n) space
        return len(nums) > len(set(nums))

        # 2nd sorting solution
        # O(nlogn) time | O(1) space
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False
