# 1st solution
# O(nlogn) time | O(n) space
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
    
# 2nd solution
# O(n) time | O(1) space
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def nsmallest(nums, n):            
            start, end = 0, len(nums)-1
            while True:
                pivot = nums[random.randint(start, end)]
                i, j, k = start, end, start
                while k <= j:
                    if nums[k] < pivot:
                        swap(nums, i, k)
                        i += 1
                        k += 1
                    elif nums[k] > pivot:
                        swap(nums, j, k)
                        j -= 1
                    else:
                        k += 1
                if i <= n - 1 <= j:
                    return pivot
                elif n - 1 < i:
                    end = i - 1
                else:
                    start = i + 1

        n = len(nums)
        mid = nsmallest(nums, (n + 1) // 2)
        # (n | 1) calculates the nearest odd that is not less than n
        mapIdx = lambda i: (1 + 2 * i) % (n | 1)
        # Three Color Sort
        left, right, k = 0, n - 1, 0
        while k <= right:
            if nums[mapIdx(k)] > mid:
                swap(nums, mapIdx(k), mapIdx(left))
                left += 1
                k += 1
            elif nums[mapIdx(k)] < mid:
                swap(nums, mapIdx(k), mapIdx(right))
                right -= 1
            else:
                k += 1