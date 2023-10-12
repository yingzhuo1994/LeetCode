class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        value = 0
        while start <= end:
            if start == end:
                value += nums[start]
            else:
                value += int(str(nums[start]) + str(nums[end]))
            start += 1
            end -= 1
        return value
