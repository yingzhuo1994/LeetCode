class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        pointer = 0
        steps = nums[pointer]
        while pointer + steps < len(nums):
            totalStep = pointer + steps
            nextPlace = pointer
            for i in range(pointer + 1, pointer + steps + 1):
                if i + nums[i] > totalStep:
                    nextPlace = i
                    totalStep = i + nums[i]
            if nextPlace == pointer:
                break
            pointer = nextPlace
            steps = nums[pointer]
        return pointer + steps >= len(nums) - 1
