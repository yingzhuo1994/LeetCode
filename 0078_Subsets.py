class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 1st recursive solution
        # O(n * 2^n) time | O(n * 2^n) space
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [[], nums]
        last = self.subsets(nums[1:])
        lst = [[nums[0]] + elem for elem in last] + last
        return lst

        # 2nd iterative solution
        # O(n * 2^n) time | O(n * 2^n) space
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output