class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, n = 0, len(nums)
        while i < n - 1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
                n -= 1
            else:
                i += 1
        return n
