# 1st solution
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def dfs(beg, end):
            if end - beg <= 1: 
                return target in nums[beg: end + 1]
            
            mid = (beg + end) // 2
            if nums[mid] > nums[end]:   # eg. 3,4,5,6,7,1,2
                if nums[end] < target <= nums[mid]:
                    return dfs(beg, mid)
                else:
                    return dfs(mid + 1, end)
            elif nums[mid] < nums[end]: # eg. 6,7,1,2,3,4,5
                if nums[mid] < target <= nums[end]:
                    return dfs(mid + 1, end)
                else:
                    return dfs(beg, mid)
            else:
                return dfs(mid+1, end) or dfs(beg, mid)
    
        return dfs(0, len(nums)-1)

# 2nd solution
# best case: O(log(n)) time | O(1) space
# worst case: O(n) time | O(1) space
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        start, end = 0, n - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return True
            
            if not self.isBinarySearchHelpful(nums, start, nums[mid]):
                start += 1
                continue
            #  which array does pivot belong to.
            pivotArray = self.existsInFirst(nums, start, nums[mid])

            #  which array does target belong to.
            targetArray = self.existsInFirst(nums, start, target)
            if (pivotArray ^ targetArray):
            # If pivot and target exist in different sorted arrays, recall that xor is true when both operands are distinct
                if pivotArray:
                    start = mid + 1 # pivot in the first, target in the second
                else:
                    end = mid - 1 # target in the first, pivot in the second
            else:
            # If pivot and target exist in same sorted array
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        return False

    # returns true if we can reduce the search space in current binary search space
    def isBinarySearchHelpful(self, arr, start, element):
        return arr[start] != element

    # returns true if element exists in first array, false if it exists in second
    def existsInFirst(self, arr, start, element):
        return arr[start] <= element