class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 1st recursive solution
        # O(n * 2^n) time | O(n * 2^n) space
        if not nums:
            return [[]]
        last = self.subsets(nums[1:])
        lst = [[nums[0]] + elem for elem in last] + last
        return lst

        # 2nd iterative solution
        # O(n * 2^n) time | O(n * 2^n) space
     def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

        # 3rd recursive solution
        # O(n * 2^n) time | O(n * 2^n) space
    def subsets(self, nums: List[int], idx = None) -> List[List[int]]:
        if idx is None:
            idx = len(nums) - 1
        if idx < 0:
            return [[]]
        elem = nums[idx]
        # avoid using list slicing array[:idx-1]
        subSets = self.subsets(nums, idx - 1)
        for i in range(len(subSets)):
            currentSubset = subSets[i]
            subSets.append(currentSubset + [elem])
        return subSets