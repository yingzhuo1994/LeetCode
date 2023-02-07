# 1st solution
# O(n) time | O(n) space
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newNums = [0] * (2 * n)
        for i in range(n):
            newNums[2*i] = nums[i]
            newNums[2*i+1] = nums[n + i]
        return newNums

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Store each y(i) with respective x(i).
        for i in range(n, 2 * n):
            secondNum = nums[i] << 10
            nums[i - n] |= secondNum

        # '0000000000 1111111111' in decimal.
        allOnes = int(pow(2, 10)) - 1

        # We will start putting all numbers from the end, 
        # as they are empty places.
        for i in reversed(range(n)):
            # Fetch both the numbers from the current index.
            secondNum = nums[i] >> 10
            firstNum = nums[i] & allOnes
            nums[2 * i + 1] = secondNum
            nums[2 * i] = firstNum
        return nums