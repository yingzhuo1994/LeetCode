class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1st solution
        # O(kn) time | O(1) space
        k = k % len(nums)
        while k > 0:
            lastValue = nums[-1]
            for i in reversed(range(1, len(nums))):
                nums[i] = nums[i - 1]
            nums[0] = lastValue
            k -= 1
        
        # 2nd solution
        # O(n) time | O(n) space
        k = k % len(nums)
        lst = nums[-k:] + nums[:-k]
        nums[:] = lst

        # 3rd solution
        # O(n) time | O(1) space
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1
        
        # 4th solution
        # o(n) time | O(1) sapce 
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums: list, start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1