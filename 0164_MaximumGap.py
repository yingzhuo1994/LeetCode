# 1st solution
# O(n*log(n)) time | O(n) space
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        nums.sort()
        ans = 0
        for i in range(n - 1):
            ans = max(ans, nums[i+1] - nums[i])
        return ans

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        low, high, n = min(nums), max(nums), len(nums)
        if n <= 2 or high == low:
            return high - low
        B = defaultdict(list)
        for num in nums:
            ind = n-2 if num == high else (num - low)*(n-1)//(high-low)
            B[ind].append(num)
            
        cands = [[min(B[i]), max(B[i])] for i in range(n-1) if B[i]]
        return max(cands[i+1][0]-cands[i][1] for i in range(len(cands) - 1))