class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 1st solution
        # O(n^2) time | O(1) space
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

        # 2nd solution
        # O(n) time | O(1) space
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True
