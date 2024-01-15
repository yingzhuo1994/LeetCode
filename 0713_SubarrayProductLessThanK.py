# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
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


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left, prod, count = 0, 1, 0

        for right, num in enumerate(nums):
            prod *= num

            while prod >= k:
                prod //= nums[left]
                left += 1
            count += right - left + 1

        return count
