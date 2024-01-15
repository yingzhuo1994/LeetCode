# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        products = [1]
        for num in nums:
            products.append(products[-1] * num)
        
        def binary_search(nums, target):
            start, end = 0, len(nums)
            while start < end:
                mid = start + (end - start) // 2
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid
            return start
        
        ans = 0
        for i in range(1, len(products)):
            if products[i] < k:
                ans += i
                print("count: ", i)
                continue
            target = products[i] // k + 1
            j = binary_search(products, target)
            ans += max(i - j, 0)

        return ans