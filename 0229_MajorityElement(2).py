# 1st solution
# O(n) time | O(n) space
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = n // 3
        count = collections.Counter(nums)
        ans = []
        for k, v in count.items():
            if v > freq:
                ans.append(k)
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [num for num in (candidate1, candidate2)
                        if nums.count(num) > len(nums) // 3]