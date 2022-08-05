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

# 3rd solution, binary search
# O(n*log(s)) time | O(1) space
# where n is the length of the array, and s is the sum of intergers in the array
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def min_subarrays_required(max_sum_allowed: int) -> int:
            current_sum = 0
            splits_required = 0
            
            for element in nums:
                # Add element only if the sum doesn't exceed max_sum_allowed
                if current_sum + element <= max_sum_allowed:
                    current_sum += element
                else:
                    # If the element addition makes sum more than max_sum_allowed
                    # Increment the splits required and reset sum
                    current_sum = element
                    splits_required += 1

            # Return the number of subarrays, which is the number of splits + 1
            return splits_required + 1
        
        # Define the left and right boundary of binary search
        left = max(nums)
        right = sum(nums)
        while left <= right:
            # Find the mid value
            max_sum_allowed = (left + right) // 2
            
            # Find the minimum splits. If splits_required is less than
            # or equal to m move towards left i.e., smaller values
            if min_subarrays_required(max_sum_allowed) <= m:
                right = max_sum_allowed - 1
                minimum_largest_split_sum = max_sum_allowed
            else:
                # Move towards right if splits_required is more than m
                left = max_sum_allowed + 1
        
        return minimum_largest_split_sum

# 4th solution, binary search
# O(n + (log(n))^2 *log(s)) time | O(1) space
# where n is the length of the array, and s is the sum of intergers in the array
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        
        for i in range(len(nums) - 1):
            nums[i+1] += nums[i]

        ans = right
        while left <= right:
            value = left + (right - left) // 2
            count = self.countArray(nums, value)
            if count <= m:
                right = value - 1
                ans = min(ans, value)
            else:
                left = value + 1

        return ans
    
    def countArray(self, nums, target):
        count = 0
        idx = 0
        newTarget = target
        while idx < len(nums):
            idx = bisect.bisect_right(nums, newTarget, lo=idx)
            count += 1
            newTarget = nums[idx-1] + target
        return count