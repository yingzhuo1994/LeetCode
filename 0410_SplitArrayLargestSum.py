# 1st solution, top-down
# O(n^2*m) time | O(nm) space
# where n is the length of the array, and m is the number of subarrays allowed.
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        
        # Create a prefix sum array of nums.
        prefix_sum = [0] + list(itertools.accumulate(nums))
        
        @functools.lru_cache(None)
        def get_min_largest_split_sum(curr_index: int, subarray_count: int):
            # Base Case: If there is only one subarray left, then all of the remaining numbers
            # must go in the current subarray. So return the sum of the remaining numbers.
            if subarray_count == 1:
                return prefix_sum[n] - prefix_sum[curr_index]
        
            # Otherwise, use the recurrence relation to determine the minimum largest subarray sum
            # between curr_index and the end of the array with subarray_count subarrays remaining.
            minimum_largest_split_sum = prefix_sum[n]
            for i in range(curr_index, n - subarray_count + 1):
                # Store the sum of the first subarray.
                first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]

                # Find the maximum subarray sum for the current first split.
                largest_split_sum = max(first_split_sum, 
                                        get_min_largest_split_sum(i + 1, subarray_count - 1))

                # Find the minimum among all possible combinations.
                minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)

                if first_split_sum >= minimum_largest_split_sum:
                    break
            
            return minimum_largest_split_sum
        
        return get_min_largest_split_sum(0, m)

# 2nd solution, bottom-up
# O(n^2*m) time | O(nm) space
# where n is the length of the array, and m is the number of subarrays allowed.
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        memo = [[0] * (m + 1) for _ in range(n)]
        
        # Create a prefix sum array of nums.
        prefix_sum = [0] + list(itertools.accumulate(nums))
        
        for subarray_count in range(1, m + 1):
            for curr_index in range(n):
                # Base Case: If there is only one subarray left, then all of the remaining numbers
                # must go in the current subarray. So return the sum of the remaining numbers.
                if subarray_count == 1:
                    memo[curr_index][subarray_count] = prefix_sum[n] - prefix_sum[curr_index]
                    continue

                # Otherwise, use the recurrence relation to determine the minimum largest subarray sum
                # between curr_index and the end of the array with subarray_count subarrays remaining.
                minimum_largest_split_sum = prefix_sum[n]
                for i in range(curr_index, n - subarray_count + 1):
                    # Store the sum of the first subarray.
                    first_split_sum = prefix_sum[i + 1] - prefix_sum[curr_index]

                    # Find the maximum subarray sum for the current first split.
                    largest_split_sum = max(first_split_sum, memo[i + 1][subarray_count - 1])

                    # Find the minimum among all possible combinations.
                    minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)

                    if first_split_sum >= minimum_largest_split_sum:
                        break
            
                memo[curr_index][subarray_count] = minimum_largest_split_sum
        
        return memo[0][m]