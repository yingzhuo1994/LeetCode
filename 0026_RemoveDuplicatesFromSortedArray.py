class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1st solution
        # O(n^2) time | O(1) space
        i, n = 0, len(nums)
        while i < n - 1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)  # pop(-1) needs O(1) and pop(k) needs O(n)
                n -= 1
            else:
                i += 1
        return n

        # 2nd solution
        # O(n) time | O(1) space
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums [j]
            else:
                j += 1
        return i + 1
