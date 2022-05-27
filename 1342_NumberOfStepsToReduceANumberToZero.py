# 1st solution
# O(1) time | O(1) space
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            steps += 1
        return steps

# 2nd solution
# O(1) time | O(1) space
class Solution:
    def numberOfSteps(self, num: int) -> int:
        return len(bin(num)) + bin(num).count("1") - 3