# 1st brute-force solution
# Time complexity: O(n) & Space complexity: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2
        dic = Counter(nums)
        for elem in dic:
            if dic[elem] > threshold:
                return elem
        return None

# 2nd Boyer-Moore Voting Algorithm
# Time complexity: O(n) & Space complexity: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
