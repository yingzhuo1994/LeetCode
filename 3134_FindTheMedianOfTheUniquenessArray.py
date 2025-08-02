# 1st solution, TLE
# O(n^2 * log(n)) time | O(n^2) space
class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        array = []
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                array.append(len(set(nums[i:i+length])))
        array.sort()
        k = len(array)
        return array[(k - 1) // 2]

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n + 1) * n // 2
        target = (total + 1) // 2
        left = 1
        right = n
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            cnt = {}
            start = 0
            for i, num in enumerate(nums):
                cnt[num] = cnt.get(num, 0) + 1
                while len(cnt) > mid:
                    cnt[nums[start]] -= 1
                    if cnt[nums[start]] == 0:
                        del cnt[nums[start]]
                    start += 1
                count += i - start + 1
            if count >= target:
                right = mid
            else:
                left = mid + 1
        return left
