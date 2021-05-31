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