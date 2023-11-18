# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        keys = sorted(count.keys())
        ans = 1
        for i in reversed(range(len(keys))):
            left = k
            freq = count[keys[i]]
            for j in reversed(range(i)):
                d = keys[i] - keys[j]
                q, r = divmod(left, d)
                if q <= count[keys[j]]:
                    freq += q
                    left = r
                else:
                    freq += count[keys[j]]
                    left = r + (q - count[keys[j]]) * d
            ans = max(ans, freq)
            if i == 0 and left == 0:
                break
        return ans
    
# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i = 0
        nums.sort()
        for j in range(len(nums)):
            k += nums[j]
            if k < nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
        return j - i + 1