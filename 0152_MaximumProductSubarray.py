# 1st brute-force solution
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = nums[0]
        for i in range(len(nums)):
            curProduct = 1
            for j in range(i, len(nums)):
                curProduct *= nums[j]
                largest = max(largest, curProduct)
        return largest

# 2nd solution
# o(n) time | O(1) space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r = nums[0]
        imax = r
        imin = r
        # imax/imin stores the max/min product of
        # subarray that ends with the current number A[i]
        for i in range(1, len(nums)):
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremums by swapping them
            if nums[i] < 0:
                imax, imin = imin, imax

            # max/min product for the current number is either the current number itself
            # or the max/min by the previous number times the current one
            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])

            # the newly computed max value is a candidate for our global result
            r = max(r, imax)
    
        return r