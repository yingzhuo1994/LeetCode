# 1st solution
# O(nlogn) time | O(1) space
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
    
# 2nd solution, bubble sort idea
# O(nk) time | O(1) space
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    # exchange elements, time consuming
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums[-k]
    
# 3rd solution, selection sort idea
# O(nk) time | o(1) space
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums), len(nums)-k, -1):
            tmp = 0
            for j in range(i):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
        return nums[-k]

# 4th solution, quick select
# O(n) time | O(n) space
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]

# 5th solution, quick select in place
# O(n) time | O(1) space
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, k)
    
    def quickSelect(self, nums, left, right, k):
        pivot = nums[left]
        L, R = left, right
        idx = L
        while idx <= R:
            if nums[idx] > pivot:
                self.swap(nums, L, idx)
                L += 1
                idx += 1
            elif nums[idx] < pivot:
                self.swap(nums, idx, R)
                R -= 1
            else:
                idx += 1
        if k <= L:
            return self.quickSelect(nums, left, L - 1, k)
        elif k > idx:
            return self.quickSelect(nums, idx, right, k)
        else:
            return pivot
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]