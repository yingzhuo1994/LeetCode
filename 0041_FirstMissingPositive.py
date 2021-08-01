class Solution:
    # 1st brute force solution
    # O(n^2) time | O(1) space
    # 'in' operation for a list, the average time complexity is O(n)
    def firstMissingPositive(self, nums: List[int]) -> int:
        k = 1
        while k in nums:
            k += 1
        return k

    # 2nd solution
    # O(n) time | O(1) space
    def firstMissingPositive(self, nums: List[int]) -> int:
        """"
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within 
            the range [1,...,l+1] 
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)): #delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)): #use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        for i in range(1, len(nums)):
            if nums[i] // n == 0:
                return i
        return n