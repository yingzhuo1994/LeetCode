# 1st solution
# O(n) time | O(1) space
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = sum(nums)
        digitSum = sum(sum(map(int, list(str(num)))) for num in nums)
        return abs(elementSum - digitSum)


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans += x  # 累加元素和
            while x:
                ans -= x % 10  # 减去数位和
                x //= 10
        return ans